
import plotly.graph_objects as go
from app.config.datas import TOTAL_DESM_21_ANOS, DT_LAST_YEAR, DT_FIRST_YEAR, DEFAULT_MUN_IBGE, DEFAULT_STAT_NAME, DEFAULT_STAT, DEFAULT_MUN, ESTADOS
from app.config.definitions import LABEL_FONT_SIZE, LABEL_CARD_SIZE, ANO_INI, ANO_FIM

class Desm21AnosLabel:

    @staticmethod
    def buildByMunDefault():
        value = [DEFAULT_MUN_IBGE, DEFAULT_MUN]
        return Desm21AnosLabel.buildByMun(value)

    @staticmethod
    def buildByMun(value):
        totalLastYear = DT_LAST_YEAR.query("CodIbge==%s"%value[0]).sum().Desmatamento
        totalFirstYear = DT_FIRST_YEAR.query("CodIbge==%s"%value[0]).sum().Desmatamento
        total = totalLastYear - totalFirstYear
        return Desm21AnosLabel.build(total, value[1])

    @staticmethod
    def buildByState(value):
        totalLastYear = DT_LAST_YEAR.query("Estado=='%s'"%value[0]).sum().Desmatamento
        totalFirstYear = DT_FIRST_YEAR.query("Estado=='%s'"%value[0]).sum().Desmatamento
        total = totalLastYear - totalFirstYear
        return Desm21AnosLabel.build(total, ESTADOS[value[0]])

    @staticmethod
    def buildByStateDefault():
        return Desm21AnosLabel.buildByState([DEFAULT_STAT, DEFAULT_STAT_NAME])

    @staticmethod
    def buildLegalAmazon():
        fig = go.Figure()
        fig.add_trace(go.Indicator(mode="number", value=TOTAL_DESM_21_ANOS, number={ 'suffix': ' km²', 'valueformat': ',.2f', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=LABEL_CARD_SIZE, title='Total desmatado entre %d e %d'%(ANO_INI, ANO_FIM))
        
        return fig

    @staticmethod
    def build(total, name):

        fig = go.Figure()
        fig.add_trace(go.Indicator(mode="number", value=total, number={ 'suffix': ' km²', 'valueformat': ',.2f', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=LABEL_CARD_SIZE, title='%s desmatou um total de'%name)
        
        return fig

