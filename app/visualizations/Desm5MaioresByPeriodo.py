
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from app.config.datas import DT_5_MAIS_PERIODO_1, DT_5_MAIS_PERIODO_2, DT_5_MAIS_PERIODO_3, DT_5_MAIS_PERIODO_4
from app.config.definitions import PRIMARY_COLOR, SECONDARY_COLOR

class Desm5MaioresByPeriodo:

    def build():
        fig = go.Figure()

        fig.add_trace(go.Bar(name='Descontrole I', x=DT_5_MAIS_PERIODO_1.Ano, 
        y=DT_5_MAIS_PERIODO_1.Incremento, text=DT_5_MAIS_PERIODO_1.Incremento, 
        textposition='outside', texttemplate='%{text:.3s}', marker_color='lightslategrey'))
        fig.add_trace(go.Bar(name='Decremento', x=DT_5_MAIS_PERIODO_2.Ano, 
                            y=DT_5_MAIS_PERIODO_2.Incremento, text=DT_5_MAIS_PERIODO_2.Incremento, 
                            textposition='outside', texttemplate='%{text:.3s}', marker_color='rgba(239, 85, 59, 0.7)'))
        fig.add_trace(go.Bar(name='Estabilidade', x=DT_5_MAIS_PERIODO_3.Ano,
                            y=DT_5_MAIS_PERIODO_3.Incremento, text=DT_5_MAIS_PERIODO_3.Incremento, 
                            textposition='outside', texttemplate='%{text:.3s}', marker_color='rgba(102, 193, 164, 0.7)'))
        fig.add_trace(go.Bar(name='Descontrole II', x=DT_5_MAIS_PERIODO_4.Ano, 
                            y=DT_5_MAIS_PERIODO_4.Incremento, text=DT_5_MAIS_PERIODO_4.Incremento, 
                            textposition='outside', texttemplate='%{text:.3s}', marker_color='rgb(55, 83, 109)'))

        fig.update_layout(title='5 Maiores cidades que desmataram')
        fig.update_xaxes(dtick="M1")
        return fig