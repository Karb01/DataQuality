import pandas as pd
import numpy as np
import os
import re

def validar_nota(df):
    """
        Valida se alguma nota de NPS chegou null ou vazia:

        Args:
            DataFrame(df): O dataframe do arquivo
        Returns:
            Pais(str): Retorna 1 caso seja identificado alguma nota nula, e 0 caso não seja identificado nenhum erro. 
    """

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
    """
        Valida se alguma nota de NPS chegou maior que 10:

        Args:
            DataFrame(df): O dataframe do arquivo
        Returns:
            Pais(str): Retorna 1 caso seja identificado alguma nota de NPS maior que 10, e 0 caso não seja identificado nenhum erro. 
    """

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
    """
        Valida se alguma nota de NPS chegou menor que 0:

        Args:
            DataFrame(df): O dataframe do arquivo
        Returns:
            Pais(str): Retorna 1 caso seja identificado alguma nota de NPS menor que 0, e 0 caso não seja identificado nenhum erro. 
    """

    if 'Nota' not in df.columns:
        return 1
    nota_convertida = pd.to_numeric(df['Nota'], errors='coerce')
    notas_invalidas = (nota_convertida < 0)
    total_erros = notas_invalidas.sum()
    if total_erros > 0:
        return 1
    else:
        return 0

