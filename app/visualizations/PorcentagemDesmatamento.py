
import plotly.graph_objects as go
from config.datas import PORC_AREA, DT_SET, DEFAULT_MUN_IBGE, ESTADOS, DEFAULT_MUN, TOTAL_DESM, DEFAULT_STAT, DEFAULT_STAT_NAME, DT_LAST_YEAR, AREA_AL
from config.definitions import LABEL_FONT_SIZE, LABEL_CARD_SIZE

class PorcentagemDesmatamento:

    
    @staticmethod
    def buildByMunDefault():
        value = [DEFAULT_MUN_IBGE, DEFAULT_MUN]
        return PorcentagemDesmatamento.buildByMun(value)

    @staticmethod
    def buildByMun(value):
        area = DT_LAST_YEAR.query("CodIbge==%s"%value[0]).sum().Desmatamento
        porc = (area/TOTAL_DESM) * 100
        return PorcentagemDesmatamento.build(porc, value[1])  

    @staticmethod
    def buildByState(value):
        area = DT_LAST_YEAR.query("Estado=='%s'"%value[0]).sum().Desmatamento
        porc = (area/TOTAL_DESM) * 100
        return PorcentagemDesmatamento.build(porc, ESTADOS[value[0]])  
    
    @staticmethod
    def buildByStateDefault():
        value = [DEFAULT_STAT, DEFAULT_STAT_NAME]  
        return PorcentagemDesmatamento.buildByState(value)
        

    @staticmethod
    def build(porc, name):
        fig = go.Figure()
        fig.add_trace(go.Indicator(mode="number", value=porc, number={ 'suffix': '%', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=LABEL_CARD_SIZE, title='Desmatamento correspondente de %s'%name)
    
        return fig
