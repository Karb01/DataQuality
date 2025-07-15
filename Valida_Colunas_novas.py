import os
import pandas as pd
import numpy as np
import re

def normalizar_colunas(colunas):
    """
        Normaliza todas as colunas para minuscula:

        Args:
            Colunas(array): Todas as colunas 
    """

    return [col.strip().lower() for col in colunas]

def validar_colunas_novas(df, colunas_esperadas):
    """
        Valida se chegou alguma coluna nova:

        Args:
            DataFrame(df): O dataframe do arquivo
            Colunas_esperadas(array): as colunas que são esperadas chegar no arquivo 
        Returns:
            bool(int): Retorna 1 se alguma das coluna nova foi inserida 0 se nenhuma coluna nova foi encontrado 
    """

    colunas_atual = set(normalizar_colunas(df.columns))
    colunas_esperadas_set = set(normalizar_colunas(colunas_esperadas))
    colunas_novas = colunas_atual - colunas_esperadas_set
    if colunas_novas:
        return 1
    else:
        return 0
