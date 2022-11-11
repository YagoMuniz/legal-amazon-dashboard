
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from app.config.datas import DT_LAST_YEAR_BY_STATE, DT_SET
from app.config.definitions import PRIMARY_COLOR, SECONDARY_COLOR

class FlorestasRestantes:

    @staticmethod
    def build():
        fig = go.Figure(go.Bar(name='', x=DT_LAST_YEAR_BY_STATE.Floresta, y=DT_LAST_YEAR_BY_STATE.Estado, 
                       text=DT_LAST_YEAR_BY_STATE.Floresta, textposition='outside', 
                       texttemplate='%{text:.3s}', orientation='h', marker=dict(
        color=PRIMARY_COLOR["color"], line=dict(color=PRIMARY_COLOR["line"], width=1))))
        fig.update_layout(margin=dict(r=25, l=50, t=50, b=50), title='Quantidade de florestas restante no final do ano de 2020', xaxis=dict(tickformat=".3s", tick0=2000))

        return fig

