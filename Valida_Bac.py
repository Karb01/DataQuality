import os
import pandas as pd
import numpy as np
import re

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
