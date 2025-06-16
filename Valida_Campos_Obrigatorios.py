import os
import pandas as pd
import numpy as np
import re

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
