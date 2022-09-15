
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from app.config.datas import DT_SET, DT_21_ANOS, DT_SET_BY_MUN_DESMATAMENTO,DEFAULT_STAT, ESTADOS, DEFAULT_STAT_NAME, DEFAULT_MUN_IBGE, DT_SET_BY_STATE_DESMATAMENTO, DT_SET_BY_STATE_FLOREST, STATES, PERC_DESMATADO, DEFAULT_MUN
from app.config.definitions import PRIMARY_COLOR, SECONDARY_COLOR, CARD_BARS_SIZE, LABEL_CARD_SIZE, LABEL_FONT_SIZE

class MaiorAnoKmLabel:

    @staticmethod
    def buildByMunDefault():
        dtSet = DT_SET_BY_MUN_DESMATAMENTO.query("CodIbge==%s"%DEFAULT_MUN_IBGE)
        value = [DEFAULT_MUN_IBGE, dtSet.Municipio.values[0], dtSet.Desmatamento.values[0]]
        return MaiorAnoKmLabel.buildByMun(value)

    @staticmethod
    def buildByMun(value):
        dtDesmatamento = DT_SET.query('CodIbge==%s'%value[0]).groupby('Ano').sum().reset_index().sort_values('Incremento', ascending=False)
        return MaiorAnoKmLabel.build(dtDesmatamento.head(1).Incremento.values[0], dtDesmatamento.head(1).Ano.values[0])

    @staticmethod
    def buildByState(value):
        dtDesmatamento = DT_SET.query("Estado=='%s'"%value[0]).groupby('Ano').sum().reset_index().sort_values('Incremento', ascending=False)
        nomeEstado = value[0]
        qtdDesmatada = value[1]
        return MaiorAnoKmLabel.build(dtDesmatamento.head(1).Incremento.values[0], dtDesmatamento.head(1).Ano.values[0])

    @staticmethod
    def buildByStateDefault():
        dtSet = DT_SET_BY_STATE_DESMATAMENTO.query("Estado=='%s'"%DEFAULT_STAT)
        return MaiorAnoKmLabel.buildByState([DEFAULT_STAT, dtSet.Desmatamento.values[0]])

    @staticmethod
    def build(qtd, ano):
        fig = go.Figure()
        fig.add_trace(go.Indicator(mode="number", value=qtd, number={ 'suffix': ' km²', 'valueformat': ',.2f', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=LABEL_CARD_SIZE, title='Desmatado em %d'%ano)
        
        return fig
        

        

        