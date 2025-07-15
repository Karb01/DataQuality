import os
import pandas as pd
import numpy as np
import re

ddi_por_pais = {
    'brasil': '55',
    'argentina': '54',
    'colombia': '57',
    'chile': '56',
    'peru': '51',
    'equador': '59',    
}

def extrair_pais_do_arquivo(nome_arquivo):
    """
        Extrai o pais a partir do nome do arquivo:

        Args:
            Nome_arquivo(str): Passado o nome do arquivo 
        Returns:
            Pais(str): Retorna o nome do pais caso encontrado, se não encontrado retorna nada
    """

    for pais in ddi_por_pais.keys():
        if pais in nome_arquivo.lower():
            return pais
    return None


def validar_ddi_telefone(df, nome_arquivo):
    """
        Valida se o DDI está coerente com o pais no qual o numero foi enviado:

        Args:
            DataFrame(df): O dataframe do arquivo
            Nome_arquivo(str): Passado o nome do arquivo
        Returns:
            Pais(str): Retorna 1 caso seja identificado algum numero com o DDI diferente do pais no qual ele foi enviado, e 0 caso não seja identificado nenhum erro. 
    """

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
