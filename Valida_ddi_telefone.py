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
