
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from config.datas import DT_SET, DT_INTR_ESTADO, DT_MAIOR_ESTADO, DT_MENOR_ESTADO 
from config.definitions import MUN_GEO, PRIMARY_COLOR, SECONDARY_COLOR

class DoisMaioresContribuidores:

    def build():

        fig = go.Figure(data=[go.Bar(name='Pará', x=DT_MAIOR_ESTADO.Ano, 
                                    y=DT_MAIOR_ESTADO.Incremento, text=DT_MAIOR_ESTADO.Incremento, 
                                    textposition='outside', texttemplate='%{text:.3s}', marker=dict(
                color=PRIMARY_COLOR["color"], line=dict(color=PRIMARY_COLOR["line"], width=1))), 
                go.Bar(name='Mato Grosso', x=DT_MENOR_ESTADO.Ano, y=DT_MENOR_ESTADO.Incremento, 
                    text=DT_MENOR_ESTADO.Incremento, textposition='outside', 
                    texttemplate='%{text:.3s}', marker=dict(
                color=SECONDARY_COLOR["color"], line=dict(color=SECONDARY_COLOR["line"], width=1)))])
        fig.update_xaxes(dtick="M1")
        fig.update_layout(title='Desmatamento dos 2 maiores estados')
        return fig