
import plotly.graph_objects as go
from app.config.datas import AREA_AL, ESTADOS, DT_LAST_YEAR, DT_SET_BY_MUN_DESMATAMENTO, DEFAULT_MUN_IBGE, DEFAULT_STAT, DEFAULT_MUN, DEFAULT_STAT_NAME
from app.config.definitions import LABEL_FONT_SIZE, LABEL_CARD_SIZE

class Area:

    @staticmethod
    def buildByMunDefault():
        value = [DEFAULT_MUN_IBGE, DEFAULT_MUN]
        return Area.buildByMun(value)

    @staticmethod
    def buildByMun(value):
        area = DT_LAST_YEAR.query("CodIbge==%s"%value[0]).AreaKm2.sum()
        return Area.build(area, value[1], "município")

    @staticmethod
    def buildByState(value):
        area = DT_LAST_YEAR.query("Estado=='%s'"%value[0]).AreaKm2.sum()
        return Area.build(area, ESTADOS[value[0]], "estado")
    
    @staticmethod
    def buildByStateDefault():
        return Area.buildByState([DEFAULT_STAT, DEFAULT_STAT_NAME])
 
    @staticmethod
    def buildLegalAmazon():
        fig = go.Figure()
        fig.add_trace(go.Indicator(mode='number', value=AREA_AL, 
            number={ 'suffix': ' km²', 'valueformat': ',.2f', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=LABEL_CARD_SIZE, title='Área da Amazônia Legal')
        
        return fig

    @staticmethod
    def build(area, name, typeData):

        fig = go.Figure()
        fig.add_trace(go.Indicator(mode='number', value=area, 
            number={ 'suffix': ' km²', 'valueformat': ',.2f', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=LABEL_CARD_SIZE, title='Área do %s de %s'%(typeData, name))
        
        return fig

