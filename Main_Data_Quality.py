from Valida_Bac import validar_bac
from Valida_Campos_Obrigatorios import validar_campos_obrigatorios
from Valida_Colunas_novas import validar_colunas_novas
from Valida_ddi_telefone import validar_ddi_telefone
from Valida_Duplicatas import validar_duplicatas
from Valida_Nota import validar_nota
from Valida_Nota import validar_nota_2
from Valida_Nota import validar_nota_3
from ManipulaArquivo import carregar
from ManipulaArquivo import mover_arquivo
import os
import shutil
import pandas as pd
import numpy as np
import re

def main():
    pasta_origem = 'C:\\Users\\Kaynan Ribeiro\\Desktop\\Git\\Data_Quality\\'
    pasta_destino = 'C:\\Users\\Kaynan Ribeiro\\Desktop\\Git\\Data_Quality\\Processados'
    colunas_obrigatorias = ['TicketID', 'Data', 'Telefone', 'Dealer']
    colunas_esperadas = ['data', 'telefone', 'bac', 'dealer', 'nota', 'resposta', 'comentario', 'ticketid']
    df, caminho_arquivo, arquivo = carregar(pasta_origem)

    bac = validar_bac(df)
    campos_obrigatoriso = validar_campos_obrigatorios(df,colunas_obrigatorias)
    colunas_novas = validar_colunas_novas(df,colunas_esperadas)
    ddi_telefone = validar_ddi_telefone(df,arquivo)
    duplicatas = validar_duplicatas(df)
    nota = validar_nota(df)
    nota_2 = validar_nota_2(df)
    nota_3 = validar_nota_3(df)

    print(bac)
    print(campos_obrigatoriso)
    print(colunas_novas)
    print(ddi_telefone)
    print(duplicatas)
    print(nota)
    print(nota_2)
    print(nota_3)

    if df is not None and caminho_arquivo:
        mover_arquivo(caminho_arquivo,pasta_destino)

if __name__ == '__main__':
    main()
