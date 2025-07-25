import os
import pandas as pd
import numpy as np
import re
import shutil

def carregar(caminho_pasta):
    """
        Busca os arquivos em uma pasta:

        Args:
            caminho_pasta(str): Caminho completo do arquivo
        Returns:
            Nome_arquivo(str): O nome dos arquivos encontrados na pasta 
    """

    arquivos = [f for f in os.listdir(caminho_pasta) if f.endswith('.xlsx')]

    if not arquivos:
        print("Nenhum arquivo encontrado")
        return None, None
    
    arquivo = arquivos[0]
    caminho_arquivo = os.path.join(caminho_pasta, arquivo)
    df = pd.read_excel(caminho_arquivo)

    print(f"Arquivo carregado: {arquivo}")
    return df, caminho_arquivo,arquivo

def mover_arquivo(origem, destino):

    """
        Move um arquivo em uma pasta para outra:

        Args:
            Origem(str): O Caminho completo do arquivo aonde ele está
            Destino(str): O Caminho para onde o arquivo vai ser enviado             
    """

    if not os.path.exists(destino):
        os.makedirs(destino)
    
    nome_arquivo = os.path.basename(origem)
    novo_caminho = os.path.join(destino, nome_arquivo)

    shutil.move(origem, novo_caminho)
    print(f"Arquivo movido para: {novo_caminho}")