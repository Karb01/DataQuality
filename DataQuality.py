import os
import pandas as pd
import numpy as np
import re

caminho_pasta = 'C:\\Users\\Kaynan Ribeiro\\Desktop\\Data_Quality\\'


## Etapas de validações

def normalizar_colunas(colunas):
    return [col.strip().lower() for col in colunas]

def carregar(caminho_pasta):
    arquivos = [f for f in os.listdir(caminho_pasta) if f.endswith('.xlsx')]

    if not arquivos:
        print("Nenhum arquivo encontrado")
        return None
    
    arquivo = arquivos[0]
    caminho_arquivo = os.path.join(caminho_pasta, arquivo)
    df = pd.read_excel(caminho_arquivo)

    print(f"Arquivo carregado: {arquivo}")
    return df, arquivo

def validar_duplicatas(df):
    qtd_duplicatas = df.duplicated().sum()
    if qtd_duplicatas > 0:
        duplicado = df[df.duplicated(keep=False)]
        return 1
    else:
        return 0

def validar_campos_obrigatorios(df, colunas_obrigatorias):
    resultado = {}
    for coluna in colunas_obrigatorias:
        if coluna not in df.columns:
            resultado[coluna] = 1
            continue

        nulos = df[coluna].isnull().sum()
        vazios = (df[coluna].astype(str).str.strip() == '').sum()

        if nulos > 0 or vazios > 0:
            resultado[coluna] = 1
        else:
            resultado[coluna] = 0
    return resultado

def extrair_pais_do_arquivo(nome_arquivo):
    for pais in ddi_por_pais.keys():
        if pais in nome_arquivo.lower():
            return pais
    return None

def validar_ddi_telefone(df, nome_arquivo):
    pais = extrair_pais_do_arquivo(nome_arquivo)
    
    if pais is None:
        return 1

    ddi_esperado = ddi_por_pais[pais]

    if 'Telefone' not in df.columns:
        return 1

    telefones = df['Telefone'].astype(str).str.strip()
    ddi_telefones = telefones.str.extract(r'^(\d{2})')[0]

    erros = (ddi_telefones != ddi_esperado).sum()

    if erros > 0:
        return 1
    else:
        return 0

def validar_colunas_novas(df, colunas_esperadas):
    colunas_atual = set(normalizar_colunas(df.columns))
    colunas_esperadas_set = set(normalizar_colunas(colunas_esperadas))
    colunas_novas = colunas_atual - colunas_esperadas_set
    if colunas_novas:
        return 1
    else:
        return 0

def validar_bac(df):
    if 'Bac' not in df.columns:
        return 1

    bac_series = df['Bac'].astype(str).str.strip()
    contem_letras = ~bac_series.str.match(r'^\d{1,6}$')
    total_erros = contem_letras.sum()
    if total_erros > 0:
        return 1
    else:
        return 0

def validar_nota(df):
    if 'Nota' not in df.columns:
        return 1
    nota_convertida = pd.to_numeric(df['Nota'], errors='coerce')
    notas_invalidas = (nota_convertida.isnull())
    total_erros = notas_invalidas.sum()
    if total_erros > 0:
        return 1
    else:
        return 0

def validar_nota_2(df):
    if 'Nota' not in df.columns:
        return 1
    nota_convertida = pd.to_numeric(df['Nota'], errors='coerce')
    notas_invalidas = (nota_convertida > 10)
    total_erros = notas_invalidas.sum()
    if total_erros > 0:
        return 1
    else:
        return 0

def validar_nota_3(df):
    if 'Nota' not in df.columns:
        return 1
    nota_convertida = pd.to_numeric(df['Nota'], errors='coerce')
    notas_invalidas = (nota_convertida < 0)
    total_erros = notas_invalidas.sum()
    if total_erros > 0:
        return 1
    else:
        return 0



## Variaveis

df, nome_arquivo = carregar(caminho_pasta)
ddi_por_pais = {
    'brasil': '55',
    'argentina': '54',
    'colombia': '57',
    'chile': '56',
    'peru': '51',
    'equador': '59',    
}

## Chamas metodos com o log

if df is not None:
    #Variaveis
    log_arquitetura = {}
    log_negocio = {}

    colunas_obrigatorias = ['TicketID', 'Data', 'Telefone', 'Dealer']
    colunas_esperadas = ['data', 'telefone', 'bac', 'dealer', 'nota', 'resposta', 'comentario', 'ticketid']
    resultado_obrigatorios = validar_campos_obrigatorios(df, colunas_obrigatorias)

    #Logs arquitetura
    log_arquitetura.update(resultado_obrigatorios)
    log_arquitetura["colunas_novas"] = validar_colunas_novas(df, colunas_esperadas)
    log_arquitetura["duplicatas"] = validar_duplicatas(df)

    #Logs de regra de negocio
    log_negocio["ddi_telefone"] = validar_ddi_telefone(df, nome_arquivo)
    log_negocio["Bac"] = validar_bac(df)
    log_negocio["nota_valida"] = validar_nota(df)
    log_negocio["nota_valida_2"] = validar_nota(df)
    log_negocio["nota_valida_3"] = validar_nota(df)
    

    print("\nValidações de Arquitetura:\n")
    for k, v in log_arquitetura.items():
        print(f"{k}: {'❌' if v == 1 else '✅'}")

    print("\nValidações de Regra de Negócio:\n")
    for k, v in log_negocio.items():
        print(f"{k}: {'❌' if v == 1 else '✅'}")

        
