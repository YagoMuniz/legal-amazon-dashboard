
import plotly.graph_objects as go
from app.config.datas import PORC_AREA, DT_SET, DEFAULT_MUN_IBGE, ESTADOS, DEFAULT_MUN, DEFAULT_STAT, DEFAULT_STAT_NAME, DT_LAST_YEAR, AREA_AL
from app.config.definitions import LABEL_FONT_SIZE, LABEL_CARD_SIZE

class PorcentagemTerriBrasil:

    
    @staticmethod
    def buildByMunDefault():
        value = [DEFAULT_MUN_IBGE, DEFAULT_MUN]
        return PorcentagemTerriBrasil.buildByMun(value)

    @staticmethod
    def buildByMun(value):
        area = DT_LAST_YEAR.query("CodIbge==%s"%value[0]).AreaKm2.sum()
        porc = (area/AREA_AL) * 100
        return PorcentagemTerriBrasil.build(porc, value[1])  

    @staticmethod
    def buildByState(value):
        area = DT_LAST_YEAR.query("Estado=='%s'"%value[0]).AreaKm2.sum()
        porc = (area/AREA_AL) * 100
        return PorcentagemTerriBrasil.build(porc, ESTADOS[value[0]])  
    
    @staticmethod
    def buildByStateDefault():
        value = [DEFAULT_STAT, DEFAULT_STAT_NAME]  
        return PorcentagemTerriBrasil.buildByState(value)
        

    @staticmethod
    def buildLegalAmazon():
        fig = go.Figure()
        fig.add_trace(go.Indicator(mode="number", value=PORC_AREA, number={ 'suffix': '%', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=LABEL_CARD_SIZE, title='Totalidade no território brasileiro')
        
        return fig

    @staticmethod
    def build(porc, name):
        fig = go.Figure()
        fig.add_trace(go.Indicator(mode="number", value=porc, number={ 'suffix': '%', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=LABEL_CARD_SIZE, title='Totalidade no território brasileiro: %s'%name)
        
        return fig
