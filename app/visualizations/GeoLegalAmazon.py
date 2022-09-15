import geopandas
import geopandas as gpd
import plotly.graph_objects as go
import plotly.express as px
import json

from config.datas import DT_SET, DT_SET_BY_STATE_DESMATAMENTO, DT_SET_BY_MUN_DESMATAMENTO
from config.definitions import MUN_GEO, STATES_GEO, GEO_DEFORESTATION, GEO_DEFORESTATION_MUN
class GeoLegalAmazon:
    @staticmethod
    def build():

        geodf = gpd.read_file(GEO_DEFORESTATION)
        geodf = geodf.to_crs("WGS84")
        geodf['center'] = geodf['geometry'].centroid
        geodf['lon'] = geodf.center.map(lambda p: p.x)
        geodf['lat'] = geodf.center.map(lambda p: p.y)
        geodf = geodf.set_index("ID")

        fig = go.Figure(go.Scattermapbox(lat=geodf.lat, lon=geodf.lon, mode='markers', hoverinfo='text', hovertext=geodf['STATE'], marker=go.scattermapbox.Marker(size=3, color="#636363")))

        # fig.update_geos(fitbounds="locations", visible=False)
        fig.update_layout(title="Áreas desmatadas em 2021", mapbox_style="carto-positron", margin={"r":0,"t":50,"l":0,"b":0}, mapbox=dict(center=dict(lat=-5.44972, lon=-57.92972),zoom=3.5))

        return fig
