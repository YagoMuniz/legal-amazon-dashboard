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

def getDtTotal():
    return DT_LAST_YEAR.sum().Desmatamento

def getStateExtensao():
    return DT_LAST_YEAR.groupby('Estado').sum().reset_index().sort_values('AreaKm2')

def getArcoDesmatamento():
    return DT_LAST_YEAR.sort_values('Desmatamento', ascending=False).head(50)

def getSetByStateDesmatamento():
    return  DT_LAST_YEAR.groupby("Estado").sum().reset_index()

def getSetByMunDesmatamento():
    return  DT_LAST_YEAR.groupby(["CodIbge", "Municipio"]).sum().reset_index()

def getSetByStateFlorest():
    return  DT_SET.query('Ano==2000').groupby('Estado').sum().reset_index()

def getDt21Anos(): 
    return DT_SET_BY_STATE_DESMATAMENTO.Desmatamento - DT_SET_BY_STATE_FLOREST.Desmatamento

def getPercDesmatamento(): 
    return DT_SET_BY_STATE_FLOREST.Desmatamento / DT_SET_BY_STATE_DESMATAMENTO.Desmatamento * 100

def getMaisDesmatamento(): 
    return DT_LAST_YEAR.sort_values('Desmatamento', ascending=False).head(5).CodIbge

def getDt5Mais(): 
    return DT_SET.query('CodIbge in @MAIS_DESM')

def getDt5MaisSoma(): 
    return DT_5_MAIS.groupby('Ano').sum().reset_index()

def getDt5MaisPeriodo1(): 
    return DT_5_MAIS_SOMA.query('Ano <= 2005')

def getDt5MaisPeriodo2(): 
    return DT_5_MAIS_SOMA.query('Ano > 2005 and Ano <= 2010')

def getDt5MaisPeriodo3(): 
    return DT_5_MAIS_SOMA.query('Ano > 2010 and Ano <= 2017')

def getDt5MaisPeriodo4(): 
    return DT_5_MAIS_SOMA.query('Ano >= 2018')

def getDtLastYearByState():
    return DT_LAST_YEAR.groupby('Estado').sum().reset_index().sort_values('Floresta', ascending=False)

def getTotalDesmatamento():
    return DT_LAST_YEAR.sum().Desmatamento

def getDesmatamentoAntesAno2000():
    return DT_FIRST_YEAR.sum().Desmatamento

def getTotalDesmatamento21Anos():
    return TOTAL_DESM - DESM_BEF_2000

def getAreaAmazoniaLegal():
    return DT_LAST_YEAR.AreaKm2.sum()



DT_SET = load_dataset() 
DT_INTR_ESTADO = getDtIntrEstado()
DT_MAIOR_ESTADO = getDtMaiorEstado()
DT_MENOR_ESTADO = getDtMenorEstado()
DT_LAST_YEAR = getDtLastYear()
DT_FIRST_YEAR = getDtFirstYear()
DT_CORRESPONDENTE = getDtCorrespondetes()

DT_TOTAL = getDtTotal()
DT_STATE_EXTENSAO = getStateExtensao()
DESM_STATES = getCountEstadosDesmatados()
DT_SUM_STATE = getSumState()
DT_ARCO = getArcoDesmatamento()

DT_SET_BY_STATE_DESMATAMENTO = getSetByStateDesmatamento()
DT_SET_BY_MUN_DESMATAMENTO = getSetByMunDesmatamento()
DT_SET_BY_STATE_FLOREST = getSetByStateFlorest()


DT_21_ANOS = getDt21Anos()
PERC_DESMATADO = getPercDesmatamento()
MAIS_DESM = getMaisDesmatamento()
DT_5_MAIS = getDt5Mais()
DT_5_MAIS_SOMA = getDt5MaisSoma()

DT_5_MAIS_PERIODO_1 = getDt5MaisPeriodo1()
DT_5_MAIS_PERIODO_2 = getDt5MaisPeriodo2()
DT_5_MAIS_PERIODO_3 = getDt5MaisPeriodo3()
DT_5_MAIS_PERIODO_4 = getDt5MaisPeriodo4()

DT_LAST_YEAR_BY_STATE = getDtLastYearByState()

TOTAL_DESM = getTotalDesmatamento()
DESM_BEF_2000 = getDesmatamentoAntesAno2000()
TOTAL_DESM_21_ANOS = getTotalDesmatamento21Anos()

AREA_AL = getAreaAmazoniaLegal()

AREA_BR = 8510345.538
PORC_AREA = (AREA_AL/AREA_BR) * 100  

DEFAULT_MUN = "Altamira"
DEFAULT_MUN_IBGE = 1500602
DEFAULT_STAT = "AC"
DEFAULT_STAT_NAME = "Acre"

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

STATES = list(DT_SET_BY_STATE_DESMATAMENTO.Estado.unique())