
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from app.config.datas import DT_5_MAIS
from app.config.definitions import PRIMARY_COLOR, SECONDARY_COLOR

class Desm5MaioresMunicipios:

    @staticmethod
    def build():
        fig = px.line(DT_5_MAIS, x=DT_5_MAIS.Ano, y=DT_5_MAIS.Incremento, color=DT_5_MAIS.Municipio, markers=True)
        fig.update_xaxes(dtick="M1")

        return fig