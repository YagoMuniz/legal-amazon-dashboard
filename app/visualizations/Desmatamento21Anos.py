
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from app.config.datas import DT_21_ANOS, DT_SET_BY_STATE_DESMATAMENTO, DT_SET_BY_STATE_FLOREST, STATES, PERC_DESMATADO
from app.config.definitions import PRIMARY_COLOR, SECONDARY_COLOR, CARD_BARS_SIZE

class Desmatamento21Anos:

    def build():
        fig = go.Figure(data=[
                go.Bar(name='Desmatado até 2000', y=DT_SET_BY_STATE_FLOREST.Desmatamento, x=STATES, 
                    text=DT_SET_BY_STATE_FLOREST.Desmatamento, textposition='outside', texttemplate='%{text:.3s}', marker=dict(
                    color=PRIMARY_COLOR["color"], line=dict(color=PRIMARY_COLOR["line"], width=1))), 
                go.Bar(name='Desmatado em 21 anos', y=DT_21_ANOS, x=STATES, text=DT_21_ANOS, textposition='outside', 
                    texttemplate='%{text:.3s}', marker=dict(
                    color=SECONDARY_COLOR["color"], line=dict(color=SECONDARY_COLOR["line"], width=1)))])
        fig.update_layout(margin=dict(r=25, l=50, t=50, b=50), legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01), title='Desmatamento no ano 2000 X Desmatamento em 21 anos')
        return fig