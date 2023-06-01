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

def questão_3(datapath):
    tabela = pd.read_csv(datapath)
    casos_por_sexo = dict(tabela["CS_SEXO"].value_counts())
    maior_quantidade = list(casos_por_sexo.keys())
    tupla = tuple(maior_quantidade[0])
    return casos_por_sexo, maior_quantidade


def questao_4(datapath):
    tabela = pd.read_csv(datapath)
    return tabela["IDADE"].mean()