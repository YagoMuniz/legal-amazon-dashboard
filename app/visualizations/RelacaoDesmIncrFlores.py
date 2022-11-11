
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from app.config.datas import DT_5_MAIS
from app.config.definitions import PRIMARY_COLOR, SECONDARY_COLOR

class Desm5MaioresMunicipios:

    def build():
        fig = px.line(DT_5_MAIS, x=DT_5_MAIS.Ano, y=DT_5_MAIS.Incremento, color=DT_5_MAIS.Municipio, markers=True)
        fig.update_xaxes(dtick="M1")

        # fig = go.Figure(data=[go.Scatter(x=DT_5_MAIS.Ano, y=DT_5_MAIS.Incremento)], 
        #     layout=go.Layout(updatemenus=[dict(type="buttons", buttons=[dict(label="Play", method="animate", args=[None])])]),
        #     frames=[go.Frame(data=[go.Scatter(x=[2000, 2000], y=[500, 700])]),
        #         go.Frame(data=[go.Scatter(x=[2000, 2002], y=[500, 900])]),
        #         go.Frame(data=[go.Scatter(x=[2000, 2003], y=[500, 1000])],
        #              layout=go.Layout(title_text="5 maiores cidades desmatadas"))])
        # fig.update_xaxes(dtick="M1")
        return fig