
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from app.config.datas import DT_SET, DT_SUM_STATE, DT_LAST_YEAR, DESM_STATES, DT_ARCO
from app.config.definitions import MUN_GEO


class ArcoDesmatamento:

    def build():

        file = open(MUN_GEO, encoding="utf8")
        geo_mun = json.load(file)
   
        fig = px.scatter_mapbox(DT_ARCO, lat=DT_ARCO.Lat, lon=DT_ARCO.Long,
                        size=DT_ARCO.Desmatamento,
                        hover_name=DT_ARCO.Municipio, color=DT_ARCO.Desmatamento,
                        hover_data=[DT_ARCO.Estado, DT_ARCO.Desmatamento],
                        color_continuous_scale=px.colors.cyclical.IceFire, 
                        size_max=15, zoom=3.5)
        fig.update_layout(mapbox_style="carto-positron")
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        return fig

