
import plotly.graph_objects as go
from config.datas import AREA_AL, ESTADOS, DT_LAST_YEAR, DT_SET_BY_MUN_DESMATAMENTO, DEFAULT_MUN_IBGE, DEFAULT_STAT, DEFAULT_MUN, DEFAULT_STAT_NAME
from config.definitions import LABEL_FONT_SIZE, LABEL_CARD_SIZE

class Title:

    @staticmethod
    def buildByMunDefault():
        value = [DEFAULT_MUN_IBGE, DEFAULT_MUN]
        return Title.buildByMun(value)

    @staticmethod
    def buildByMun(value):
        return value[1]

    @staticmethod
    def buildByState(value):
        return ESTADOS[value[0]]
    
    @staticmethod
    def buildByStateDefault():
        return DEFAULT_STAT_NAME

  
    @staticmethod
    def buildLegalAmazon():
        return "Amazônia Legal"