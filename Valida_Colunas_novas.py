import os
import pandas as pd
import numpy as np
import re

def normalizar_colunas(colunas):
    return [col.strip().lower() for col in colunas]

def validar_colunas_novas(df, colunas_esperadas):
    colunas_atual = set(normalizar_colunas(df.columns))
    colunas_esperadas_set = set(normalizar_colunas(colunas_esperadas))
    colunas_novas = colunas_atual - colunas_esperadas_set
    if colunas_novas:
        return 1
    else:
        return 0
