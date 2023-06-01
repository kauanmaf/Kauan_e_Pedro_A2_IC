AUTORES = ["Kauan Mariani Ferreira", "Pedro Henrique Coterli"]

import pandas as pd
import numpy as np
import matplotlib as plt

def questao_1(datapath):
    tabela = pd.read_csv(datapath)
    tamanho = len(tabela.index)
    return tamanho

def questao_2(datapath):
    tabela = pd.read_csv(datapath)
    return tabela.value_counts("ID_MUNICIP")



def questao_4(datapath):
    tabela = pd.read_csv(datapath)
    return tabela["IDADE"].mean()