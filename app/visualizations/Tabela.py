
import plotly.graph_objects as go
from dash import Dash, Input, Output, callback, dash_table
from config.datas import PORC_AREA, DT_SET, DEFAULT_MUN_IBGE, ESTADOS, DT_SET_BY_MUN_DESMATAMENTO, DEFAULT_MUN, TOTAL_DESM, DEFAULT_STAT, DEFAULT_STAT_NAME, DT_LAST_YEAR, AREA_AL
from config.definitions import LABEL_FONT_SIZE, LABEL_CARD_SIZE

class Tabela:

    
    @staticmethod
    def buildByMunDefault():
        value = [DEFAULT_MUN_IBGE]
        return Tabela.buildByMun(value)

    @staticmethod
    def buildByMun(value):
        data = DT_SET.query("CodIbge==%s"%value[0])
        # data = data.loc[:, data.columns.isin(['Ano', 'Incremento', 'Desmatamento', 'Floresta'])]
        # reindexData = data.reindex(columns=['Ano', 'Incremento', 'Desmatamento', 'Floresta'])
        return Tabela.build(data)  

    @staticmethod
    def buildByState(value):
        data = DT_SET.query("Estado=='%s'"%value[0]).groupby('Ano').sum().reset_index()
        return Tabela.build(data)  
    
    @staticmethod
    def buildByStateDefault():
        value = [DEFAULT_STAT]  
        return Tabela.buildByState(value)
        

    @staticmethod
    def build(data):
        fig = go.Figure(data=[go.Table(header=dict(values=['Ano', 'Desmatado', 'Acumulado', 'Florestas restantes']), 
            cells=dict(values=[data.Ano, data.Incremento, data.Desmatamento, data.Floresta], align='left'))])
        fig.update_layout(title="Informações")
        return fig
        # return dash_table.DataTable(data.to_dict('records'), [{"name": i, "id": i} for i in data.columns], id='tbl', style_cell=dict(textAlign='left'))
