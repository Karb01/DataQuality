import os
import pandas as pd
import numpy as np
import re

def validar_duplicatas(df):
    qtd_duplicatas = df.duplicated().sum()
    if qtd_duplicatas > 0:
        duplicado = df[df.duplicated(keep=False)]
        return 1
    else:
        return 0

