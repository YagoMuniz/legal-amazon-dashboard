
import plotly.graph_objects as go
from dash import Dash, Input, Output, callback, dash_table
from app.config.datas import PORC_AREA, DT_SET, DEFAULT_MUN_IBGE, ESTADOS, DT_SET_BY_MUN_DESMATAMENTO, DEFAULT_MUN, TOTAL_DESM, DEFAULT_STAT, DEFAULT_STAT_NAME, DT_LAST_YEAR, AREA_AL
from app.config.definitions import LABEL_FONT_SIZE, LABEL_CARD_SIZE

class Tabela:

    
    @staticmethod
    def buildByMunDefault():
        value = [DEFAULT_MUN_IBGE, DEFAULT_MUN]
        return Tabela.buildByMun(value)

    @staticmethod
    def buildByMun(value):
        data = DT_SET.query("CodIbge==%s"%value[0])
        nome = value[1]
        return Tabela.build(data, nome)  

    @staticmethod
    def buildByState(value):
        data = DT_SET.query("Estado=='%s'"%value[0]).groupby('Ano').sum().reset_index()
        nome = ESTADOS[value[0]]
        return Tabela.build(data, nome)  
    
    @staticmethod
    def buildByStateDefault():
        value = [DEFAULT_STAT, DEFAULT_STAT_NAME]  
        return Tabela.buildByState(value)
        

    @staticmethod
    def build(data, nome):
        fig = go.Figure(data=[go.Table(header=dict(values=['Ano', 'Desmatado', 'Florestas restantes']), 
            cells=dict(values=[data.Ano, data.Incremento, data.Floresta], align='left'))])
        fig.update_layout(margin=dict(r=50, l=50, t=50, b=50), title="Informações de %s"%nome)
        return fig
