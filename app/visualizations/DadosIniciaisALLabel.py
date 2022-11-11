
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from app.config.datas import DT_SET, DT_21_ANOS, DT_SET_BY_MUN_DESMATAMENTO,DEFAULT_STAT, ESTADOS, DEFAULT_STAT_NAME, DEFAULT_MUN_IBGE, DT_SET_BY_STATE_DESMATAMENTO, DT_SET_BY_STATE_FLOREST, STATES, PERC_DESMATADO, DEFAULT_MUN
from app.config.definitions import PRIMARY_COLOR, SECONDARY_COLOR, CARD_BARS_SIZE, LABEL_CARD_SIZE, LABEL_FONT_SIZE

class DadosIniciaisALLabel:

    # @staticmethod
    # def build():
    #     dtSetQuery = DT_SET.query("Ano==2000")
    #     hidrografia = dtSetQuery.Hidrografia.sum()
    #     nao_floresta = dtSetQuery.NaoFloresta.sum()
    #     nao_observado = dtSetQuery.NaoObservado.sum()
    #     floresta = dtSetQuery.Floresta.sum()
    #     desmatado = dtSetQuery.Incremento.sum()
    #     mun = dtSetQuery.sort_values("Incremento", ascending=False).head(1).Municipio.values[0]
    #     esta = dtSetQuery.groupby('Estado').sum().sort_values("Incremento", ascending=False).head(1).reset_index().Estado.values[0]
        
    #     value1 = ['Hidrografia', 'Áreas não florestadas', 'Áreas não observadas', 'Florestas', 'Desmatado (Km²)', 'Município com maior desmatamento', 'Estado com maior desmatamento']
    #     value2 = [hidrografia, nao_floresta, nao_observado, floresta, desmatado, mun, esta]

    #     df = pd.DataFrame(list(zip(value1, value2)), columns=['Label', 'Informacao'])

    #     fig = go.Figure(data=[go.Table(header=dict(values=['Label', 'Informação']), 
    #         cells=dict(values=[df.Label, df.Informacao], align='left'))])
    #     fig.update_layout(title="Informações")

    #     return fig
    
    @staticmethod    
    def buildHidro():
        dtSetQuery = DT_SET.query("Ano==2000")
        hidrografia = dtSetQuery.Hidrografia.sum()

        fig = go.Figure()
        fig.add_trace(go.Indicator(mode="number", value=hidrografia, number={ 'suffix': ' km²', 'valueformat': ',.2f', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=85, title='Hidrografia')

        return fig
        
        