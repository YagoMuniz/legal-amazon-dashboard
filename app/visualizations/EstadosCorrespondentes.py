
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from config.datas import DT_SET, DT_SUM_STATE, DT_LAST_YEAR, DESM_STATES
from config.definitions import MUN_GEO


class EstadosCorrespondentes:

    def build():

        dtCorrespondente = DT_LAST_YEAR
        estados = list(DT_SUM_STATE[0:DESM_STATES[1]].Estado)
        dtCorrespondente['Desmatado'] = np.where(dtCorrespondente.Estado.isin(estados), 
                                         'TOTAL DESMATADO', 'RESTANTE DA AMAZÔNIA LEGAL')
        file = open(MUN_GEO, encoding="utf8")
        geo_mun = json.load(file)
   
        fig = px.choropleth(dtCorrespondente, geojson=geo_mun, 
                    locations=dtCorrespondente.CodIbge, 
                    color=dtCorrespondente.Desmatado, 
                    color_discrete_sequence=['#66c1a4', '#b3b3b3'], 
                    labels={"Desmatado": "Distribuição"},
                           center={"lat": -5.44972, "lon": -47.92972}, 
                    hover_data=["CodIbge", "Municipio", "Desmatamento"],
                          featureidkey="properties.id")

        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(title_text='Quantidade desmatada X Área dos estados')
        fig.update_traces(marker_line_width=0)
        return fig

