
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from app.config.datas import DT_SET, DT_21_ANOS, DT_SET_BY_MUN_DESMATAMENTO,DEFAULT_STAT, ESTADOS, DEFAULT_STAT_NAME, DEFAULT_MUN_IBGE, DT_SET_BY_STATE_DESMATAMENTO, DT_SET_BY_STATE_FLOREST, STATES, PERC_DESMATADO, DEFAULT_MUN
from app.config.definitions import PRIMARY_COLOR, SECONDARY_COLOR, CARD_BARS_SIZE

class DesmBarra:

    @staticmethod
    def buildByMunDefault():
        dtSet = DT_SET_BY_MUN_DESMATAMENTO.query("CodIbge==%s"%DEFAULT_MUN_IBGE)
        value = [DEFAULT_MUN_IBGE, dtSet.Municipio.values[0], dtSet.Desmatamento.values[0]]
        return DesmBarra.buildByMun(value)

    @staticmethod
    def buildByMun(value):
        dtDesmatamento = DT_SET.query('CodIbge==%s'%value[0]).groupby('Ano').sum().reset_index()
        nomeCidade = value[1]
        qtdDesmatada = value[2]

        return DesmBarra.build(dtDesmatamento, nomeCidade, qtdDesmatada)

    @staticmethod
    def buildByState(value):
        dtDesmatamento = DT_SET.query("Estado=='%s'"%value[0]).groupby('Ano').sum().reset_index()
        nomeEstado = value[0]
        qtdDesmatada = value[1]
        return DesmBarra.build(dtDesmatamento, ESTADOS[value[0]], qtdDesmatada)

    @staticmethod
    def buildByStateDefault():
        dtSet = DT_SET_BY_STATE_DESMATAMENTO.query("Estado=='%s'"%DEFAULT_STAT)
        return DesmBarra.buildByState([DEFAULT_STAT, dtSet.Desmatamento.values[0]])

    @staticmethod
    def build(dtDesmatamento, nome, qtdDesmatada):
        fig = go.Figure(data=[go.Bar(name='Incremento', y=dtDesmatamento.Incremento, x=dtDesmatamento.Ano, 
            text=dtDesmatamento.Incremento, textposition='outside', texttemplate='%{text:.3s} km²', marker=dict(
            color=PRIMARY_COLOR["color"], line=dict(color=PRIMARY_COLOR["line"], width=1)))])
        fig.update_xaxes(dtick="M1")
        fig.update_layout(title='%s: Desmatamento 2000 - 2020  (%.2f km²)'%(nome, qtdDesmatada))
        return fig
        

        

        