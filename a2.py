AUTORES = ["Kauan Mariani Ferreira", "Pedro Henrique Coterli"]

import pandas as pd
import numpy as np
# import matplotlib as plt

DATA = "esquistossomose.parquet"

def questao_1(datapath = DATA):
    tabela = pd.read_parquet(datapath)
    tamanho = len(tabela.index)
    return tamanho

def questao_2(datapath = DATA):
    tabela = pd.read_parquet(datapath)
    return tabela.value_counts("ID_MUNICIP")



def questao_4(datapath = DATA):
    tabela = pd.read_parquet(datapath)
    return tabela["IDADE"].mean()

def questao_5(datapath = DATA):
    tabela = pd.read_parquet(datapath)
    tabela_por_estado = tabela.value_counts("SG_UF_NOT")
    codigos_estados = {35: 'SP', 41: 'PR', 42: 'SC', 43: 'RS', 50: 'MS', 11: 'RO', 12: 'AC', 13: 'AM', 14: 'RR', 15: 'PA', 16: 'AP', 17: 'TO', 21: 'MA', 24: 'RN', 25: 'PB', 26: 'PE', 27: 'AL', 28: 'SE', 29: 'BA', 31: 'MG', 33: 'RJ', 51: 'MT', 52: 'GO', 53: 'DF', 22: 'PI', 23: 'CE', 32: 'ES'}
    for codigo, sigla in codigos_estados.items():
        tabela_por_estado.rename(index = {codigo: sigla}, inplace = True)
    return tabela_por_estado.to_dict()

def questao_6(datapath = DATA):
    tabela = pd.read_parquet(datapath)
    sexo_masculino = tabela[tabela["CS_SEXO"] == "M"]
    sexo_masculino_por_estado = sexo_masculino.value_counts("SG_UF_NOT")
    codigos_estados = {35: 'SP', 41: 'PR', 42: 'SC', 43: 'RS', 50: 'MS', 11: 'RO', 12: 'AC', 13: 'AM', 14: 'RR', 15: 'PA', 16: 'AP', 17: 'TO', 21: 'MA', 24: 'RN', 25: 'PB', 26: 'PE', 27: 'AL', 28: 'SE', 29: 'BA', 31: 'MG', 33: 'RJ', 51: 'MT', 52: 'GO', 53: 'DF', 22: 'PI', 23: 'CE', 32: 'ES'}
    for codigo, sigla in codigos_estados.items():
        sexo_masculino_por_estado.rename(index = {codigo: sigla}, inplace = True)
    return sexo_masculino_por_estado.to_dict()



def questao_8(datapath = DATA):
    tabela = pd.read_parquet(datapath)
    tabela["DT_NOTIFICACAO"] = pd.to_datetime(tabela["DT_NOTIFIC"])
    tabela["DT_SINTOMAS"] = pd.to_datetime(tabela["DT_SIN_PRI"])
    tabela["ATRASO_NOT"] = tabela["DT_NOTIFICACAO"] - tabela["DT_SINTOMAS"]
    return tabela