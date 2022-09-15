import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from app.config.definitions import DATASET_PATH, ANO_INI, ANO_FIM 

def load_dataset():
    datasets = []
    for ano in range(ANO_INI, ANO_FIM+1):
        dtSet = pd.read_csv('%s%s.csv' % ( DATASET_PATH, ano), encoding='ISO-8859-1')
        dtSet['Ano'] = ano
        dtSet.columns = ['Nr', 'Lat', 'Long', 'Latgms', 'Longms','Municipio', 
                        'CodIbge', 'Estado', 'AreaKm2', 'Desmatamento', 
                        'Incremento', 'Floresta', 'Nuvem', 'NaoObservado', 
                        'NaoFloresta', 'Hidrografia', 'Soma', 'Ano']
        datasets.append(dtSet.fillna(0))
    return pd.concat(datasets)

def dropDatasetUseless(listaColumnsDrop, ano=''):
    for col in listaColumnsDrop:
        if col in DT_SET.columns:
            DT_SET.drop(col + ano, inplace=True, axis=1)


def getDtIntrEstado():
    return DT_SET.groupby(["Estado", "Ano"] ).sum().reset_index().sort_values('Incremento', ascending=False)

def getDtMaiorEstado(): 
    return DT_INTR_ESTADO.query("Estado=='PA'").groupby('Ano').sum().reset_index()
    
def getDtMenorEstado(): 
    return DT_INTR_ESTADO.query("Estado=='MT'").groupby('Ano').sum().reset_index()

def getDtLastYear():
    return DT_SET.query('Ano==%s'%ANO_FIM)

def getDtFirstYear():
    return DT_SET.query('Ano==%s'%ANO_INI)

def getDtCorrespondetes():
    return getDtLastYear()
    
def getCountEstadosDesmatados():
    soma = 0
    countEstados = 0
    for row in DT_STATE_EXTENSAO.AreaKm2.values:
        if soma + row <= DT_TOTAL:
            soma += row
            countEstados += 1
    return (soma, countEstados)


def getSumState():
    return DT_LAST_YEAR.groupby('Estado').sum().reset_index().sort_values('AreaKm2')


ESTADOS = {
    "AC": "Acre",
    "AP": "Amapá",
    "AM": "Amazonas",
    "MA": "Maranhão",
    "MT": "Mato Grosso",
    "PA": "Pará",
    "RO": "Rondônia",
    "RR": "Roraima",
    "TO": "Tocantins"
}
DT_SET = load_dataset() 
DT_INTR_ESTADO = getDtIntrEstado()
DT_MAIOR_ESTADO = getDtMaiorEstado()
DT_MENOR_ESTADO = getDtMenorEstado()
DT_LAST_YEAR = getDtLastYear()
DT_FIRST_YEAR = getDtFirstYear()
DT_CORRESPONDENTE = getDtCorrespondetes()
DT_TOTAL = DT_LAST_YEAR.sum().Desmatamento
DT_STATE_EXTENSAO = DT_LAST_YEAR.groupby('Estado').sum().reset_index().sort_values('AreaKm2')
DESM_STATES = getCountEstadosDesmatados()
DT_SUM_STATE = getSumState()
DT_ARCO = DT_LAST_YEAR.sort_values('Desmatamento', ascending=False).head(50)

DT_SET_BY_STATE_DESMATAMENTO = DT_LAST_YEAR.groupby("Estado").sum().reset_index()
DT_SET_BY_MUN_DESMATAMENTO = DT_LAST_YEAR.groupby(["CodIbge", "Municipio"]).sum().reset_index()
DT_SET_BY_STATE_FLOREST = DT_SET.query('Ano==2000').groupby('Estado').sum().reset_index()

DT_21_ANOS = DT_SET_BY_STATE_DESMATAMENTO.Desmatamento - DT_SET_BY_STATE_FLOREST.Desmatamento
STATES = list(DT_SET_BY_STATE_DESMATAMENTO.Estado.unique())
PERC_DESMATADO = DT_SET_BY_STATE_FLOREST.Desmatamento / DT_SET_BY_STATE_DESMATAMENTO.Desmatamento *100
MAIS_DESM = DT_LAST_YEAR.sort_values('Desmatamento', ascending=False).head(5).CodIbge
DT_5_MAIS = DT_SET.query('CodIbge in @MAIS_DESM')
DT_5_MAIS_SOMA = DT_5_MAIS.groupby('Ano').sum().reset_index()
DT_5_MAIS_PERIODO_1 = DT_5_MAIS_SOMA.query('Ano <= 2005')
DT_5_MAIS_PERIODO_2 = DT_5_MAIS_SOMA.query('Ano > 2005 and Ano <= 2010')
DT_5_MAIS_PERIODO_3 = DT_5_MAIS_SOMA.query('Ano > 2010 and Ano <= 2017')
DT_5_MAIS_PERIODO_4 = DT_5_MAIS_SOMA.query('Ano >= 2018')
DT_LAST_YEAR_BY_STATE = DT_LAST_YEAR.groupby('Estado').sum().reset_index().sort_values('Floresta', ascending=False)
AREA_AL = DT_LAST_YEAR.AreaKm2.sum()
AREA_BR = 8510345.538
PORC_AREA = (AREA_AL/AREA_BR) * 100  
TOTAL_DESM = DT_LAST_YEAR.sum().Desmatamento
DESM_BEF_2000 = DT_FIRST_YEAR.sum().Desmatamento
TOTAL_DESM_21_ANOS = TOTAL_DESM - DESM_BEF_2000
DEFAULT_MUN = "Altamira"
DEFAULT_MUN_IBGE = 1500602
DEFAULT_STAT = "AC"
DEFAULT_STAT_NAME = "Acre"