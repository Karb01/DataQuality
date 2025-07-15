import os
import pandas as pd
import numpy as np
import re

def validar_campos_obrigatorios(df, colunas_obrigatorias):
    """
        Valida se todos os campos obrigatorios do arquivo estão preenchidos corretamentes:

        Args:
            DataFrame(df): O dataframe do arquivo
            Colunas_Obrigatorias(array): as colunas que são consideradas obrigatorias no arquivo 
        Returns:
            bool(int): Retorna um array indicando 1 se alguma das colunas não foi preenchida e a qual coluna foi e 0 se nenhum erro foi encontrado 
    """

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
