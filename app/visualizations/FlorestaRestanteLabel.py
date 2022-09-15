
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from config.datas import DT_SET, DT_LAST_YEAR, DT_21_ANOS, DT_SET_BY_MUN_DESMATAMENTO,DEFAULT_STAT, ESTADOS, DEFAULT_STAT_NAME, DEFAULT_MUN_IBGE, DT_SET_BY_STATE_DESMATAMENTO, DT_SET_BY_STATE_FLOREST, STATES, PERC_DESMATADO, DEFAULT_MUN
from config.definitions import PRIMARY_COLOR, SECONDARY_COLOR, CARD_BARS_SIZE, LABEL_CARD_SIZE, LABEL_FONT_SIZE

class FlorestaRestanteLabel:

    @staticmethod
    def buildByMunDefault():
        return FlorestaRestanteLabel.buildByMun([DEFAULT_MUN_IBGE])

    @staticmethod
    def buildByMun(value):
        floresta = DT_LAST_YEAR.query('CodIbge==%s'%value[0]).Floresta.values[0]
        return FlorestaRestanteLabel.build(floresta)

    @staticmethod
    def buildByState(value):
        floresta = DT_LAST_YEAR.query("Estado=='%s'"%value[0]).sum().Floresta
        return FlorestaRestanteLabel.build(floresta)

    @staticmethod
    def buildByStateDefault():
        return FlorestaRestanteLabel.buildByState([DEFAULT_STAT])

    @staticmethod
    def build(floresta):
        fig = go.Figure()
        fig.add_trace(go.Indicator(mode="number", value=floresta, number={'suffix': ' km²', 'valueformat': ',.2f', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=LABEL_CARD_SIZE, title='Floresta restante')
        
        return fig
        

        

        