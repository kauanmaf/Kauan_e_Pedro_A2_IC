AUTORES = ["Kauan Mariani Ferreira", "Pedro Henrique Coterli"]

import pandas as pd
import numpy as np
import matplotlib as plt

def questao_1(datapath):
    tabela = pd.read_csv(datapath)
    tamanho = len(tabela.index)
    return tamanho

