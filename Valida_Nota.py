import pandas as pd
import numpy as np
import os
import re

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

