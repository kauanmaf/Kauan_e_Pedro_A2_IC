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

def questão_3(datapath = DATA):
    tabela = pd.read_parquet(datapath)
    casos_por_sexo = dict(tabela["CS_SEXO"].value_counts())
    maior_quantidade = list(casos_por_sexo.keys())
    tupla = tuple(maior_quantidade[0])
    return casos_por_sexo, maior_quantidade

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

def questao_7(datapath = DATA):
    tabela = pd.read_parquet(datapath)
    mun_por_est = {31 : 853, 35 : 645, 43 : 497, 29 : 417, 41 : 399, 42 : 295, 52 : 246, 22 : 224, 25 : 223, 21: 217, 26 : 184, 23 : 184, 24 : 167, 15 : 144, 51 : 141, 17 : 139, 27 : 102, 33 : 92, 50 : 79, 32 : 78, 28 : 75, 13 : 62,11 : 52, 12 : 22, 16 : 16, 14 : 15}
    codigo_estados = {35: ' SP', 41: ' PR', 42: ' SC', 43: ' RS', 50: ' MS', 11: ' RO', 12: ' AC', 13: ' AM',14: ' RR', 15: ' PA', 16: ' AP', 17: ' TO', 21: ' MA', 24: ' RN', 25: ' PB', 26: ' PE', 27: ' AL', 28: ' SE', 29: ' BA', 31: ' MG', 33: ' RJ', 51: ' MT', 52: ' GO', 53: ' DF', 22: ' PI', 23: ' CE', 32: ' ES'}

    casos_por_estado = tabela.groupby('SG_UF_NOT')['ID_MUNICIP'].nunique()
    tabela_auxiliar = pd.DataFrame({"COD": mun_por_est.keys(), "Quantidade de Cidades": mun_por_est.values()})
    tabela_auxiliar["Quantidade de casos"] = tabela_auxiliar["COD"].map(casos_por_estado).fillna(0)
    tabela_auxiliar["Porcentagem"] = (tabela_auxiliar["Quantidade de casos"]*100/tabela_auxiliar["Quantidade de Cidades"]).round(2)
    tabela_auxiliar["UF"] = tabela_auxiliar["COD"].map(codigo_estados)
    dicionario = dict(zip(tabela_auxiliar["UF"], tabela_auxiliar["Porcentagem"]))
    return dicionario 

def questao_8(datapath = DATA):
    tabela = pd.read_parquet(datapath)
    tabela["DT_NOTIFICACAO"] = pd.to_datetime(tabela["DT_NOTIFIC"])
    tabela["DT_SINTOMAS"] = pd.to_datetime(tabela["DT_SIN_PRI"])
    tabela["ATRASO_NOT"] = tabela["DT_NOTIFICACAO"] - tabela["DT_SINTOMAS"]
    return tabela