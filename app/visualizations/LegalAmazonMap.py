
import pandas as pd
import numpy as np
import requests, json
import plotly.express as px
import plotly.graph_objects as go

from app.config.datas import DT_SET, DT_SET_BY_STATE_DESMATAMENTO, DT_SET_BY_MUN_DESMATAMENTO
from app.config.definitions import MUN_GEO, STATES_GEO


class LegalAmazonMap:

    @staticmethod
    def buildLegalAmazon():
        file = open(MUN_GEO, encoding="utf8")
        geo_mun = json.load(file)
        fig = px.choropleth_mapbox(DT_SET, geojson=geo_mun, locations=DT_SET.CodIbge, color_discrete_sequence=["#66c1a4"],
                           center={"lat": -5.44972, "lon": -57.92972}, hover_data=["CodIbge", "Municipio", "Estado"],
                          featureidkey="properties.id", zoom=3)

        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(mapbox_style="carto-positron", title="Amazônia Legal: Expansão Territorial", margin={"r":0,"t":50,"l":0,"b":0}, 
            showlegend=False)
        fig.update_traces(marker_line_width=0)
        
        return fig

    @staticmethod
    def buildByMun():
        file = open(MUN_GEO, encoding="utf8")
        geo_mun = json.load(file)
        return LegalAmazonMap.build(geo_mun, DT_SET_BY_MUN_DESMATAMENTO, DT_SET_BY_MUN_DESMATAMENTO.CodIbge, 
            "properties.id", ["CodIbge", "Municipio", "Desmatamento"])

    @staticmethod
    def buildByState():
        file = open(STATES_GEO, encoding="utf-8")
        geo_state = json.load(file)

        return LegalAmazonMap.build(geo_state, DT_SET_BY_STATE_DESMATAMENTO, DT_SET_BY_STATE_DESMATAMENTO.Estado, 
            "properties.sigla", ["Estado", "Desmatamento"])

    @staticmethod
    def build(geo, dt_set, location, key, hover_data):
        
        fig = px.choropleth_mapbox(dt_set, geojson=geo, locations=location, color_continuous_scale=["#2c7fb8", "#7fcdbb", "#edf8b1"], 
            color=dt_set.Desmatamento,
            center={"lat": -5.44972, "lon": -57.92972}, hover_data=hover_data, opacity=1,
            featureidkey=key, zoom=3.5)
        
        fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(mapbox_style="carto-positron", margin={"r":0,"t":0,"l":0,"b":0}, showlegend=False, uirevision="constant")
        
        return fig

   
