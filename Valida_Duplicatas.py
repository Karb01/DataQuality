import os
import pandas as pd
import numpy as np
import re

def validar_duplicatas(df):
    """
        Valida se alguma linha duplicada foi enviada no arquivo:

        Args:
            DataFrame(df): O dataframe do arquivo
        Returns:
            Pais(str): Retorna 1 caso seja identificado alguma duplicata, e 0 caso não seja identificado nenhum erro. 
    """

    qtd_duplicatas = df.duplicated().sum()
    if qtd_duplicatas > 0:
        duplicado = df[df.duplicated(keep=False)]
        return 1
    else:
        return 0

