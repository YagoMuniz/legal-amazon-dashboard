
import plotly.graph_objects as go
from app.config.datas import TOTAL_DESM, DT_LAST_YEAR, DEFAULT_MUN_IBGE, DEFAULT_STAT, DEFAULT_STAT_NAME, DEFAULT_MUN, ESTADOS
from app.config.definitions import LABEL_FONT_SIZE, LABEL_CARD_SIZE, ANO_FIM

class TotalDesmatado:

    @staticmethod
    def buildLegalAmazon():
        fig = go.Figure()
        fig.add_trace(go.Indicator(mode="number", value=TOTAL_DESM, number={ 'suffix': ' km²', 'valueformat': ',.2f', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=LABEL_CARD_SIZE, title='Total desmatado até o ano de %d'%ANO_FIM)
        return fig

    @staticmethod
    def build(total, name):

        fig = go.Figure()
        fig.add_trace(go.Indicator(mode="number", value=total, 
            number={ 'suffix': ' km²', 'valueformat': ',.2f', 'font':{'size':LABEL_FONT_SIZE}}))
        fig.update_layout(height=LABEL_CARD_SIZE, title='%s desmatou um total de'%name)
        
        return fig