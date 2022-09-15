

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output, State, ClientsideFunction
from visualizations.LegalAmazonMap import LegalAmazonMap
from visualizations.DoisMaioresContribuidores import DoisMaioresContribuidores as dmc
from visualizations.EstadosCorrespondentes import EstadosCorrespondentes as ec
from visualizations.ArcoDesmatamento import ArcoDesmatamento as ad
from visualizations.Desmatamento21Anos import Desmatamento21Anos as desm21Anos
from visualizations.Desm5MaioresMunicipios import Desm5MaioresMunicipios as desm5mais
from visualizations.Desm5MaioresByPeriodo import Desm5MaioresByPeriodo as desm5maisPeriodo
from visualizations.FlorestasRestantes import FlorestasRestantes as florestasRestantes
from visualizations.Area import Area
from visualizations.Title import Title
from visualizations.Desm21AnosLabel import Desm21AnosLabel
from visualizations.PorcentagemTerriBrasil import PorcentagemTerriBrasil
from visualizations.PorcentagemDesmatamento import PorcentagemDesmatamento
from visualizations.TotalDesmatado import TotalDesmatado
from visualizations.DesmBarra import DesmBarra
from visualizations.MaiorAnoLabel import MaiorAnoLabel
from visualizations.MaiorAnoKmLabel import MaiorAnoKmLabel
from visualizations.FlorestaRestanteLabel import FlorestaRestanteLabel
from visualizations.Tabela import Tabela
from visualizations.GeoLegalAmazon import GeoLegalAmazon
from flask import Flask

from config.datas import ESTADOS

import locale
locale.setlocale(locale.LC_NUMERIC, '')
locale._override_localeconv = {'thousands_sep':'.'}

dashConfig = {"displayModeBar": False, "showTips": False}

server = Flask(__name__)
app = Dash(server=server, external_stylesheets=[dbc.themes.BOOTSTRAP], external_scripts=["https://cdnjs.cloudflare.com/ajax/libs/dragula/3.7.2/dragula.min.js"])

mapa = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph( id='lam-map', figure=LegalAmazonMap.buildLegalAmazon(), config=dashConfig )]
        )
    ]
)


mapa_mun = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph( id='lam-map-mun', figure=LegalAmazonMap.buildByMun(), config=dashConfig )]
        )
    ]
)

map_state = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph( id='lam-map-state', figure=LegalAmazonMap.buildByState(), config=dashConfig )]
        )
    ]
)

mapa_arco = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph( id='arco-desm', figure=GeoLegalAmazon.build(), config=dashConfig )]
        )
    ]
)

florestas = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph( id='florestasRestantes', figure=florestasRestantes.build(), config=dashConfig)]
        )
    ]
)

cidades = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph( id='desm5mais', figure=desm5mais.build(), config=dashConfig )]
        )
    ]
)

desmatamento21anos = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph( id='desm21Anos', figure=desm21Anos.build(), config=dashConfig )]
        )
    ]
)

area = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='area', figure=Area.buildLegalAmazon())],
            
        )
    ]
)

area_mun = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='area-mun', figure=Area.buildByMunDefault())],
            
        )
    ]
)

area_state = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='area-state', figure=Area.buildByStateDefault())],
            
        )
    ]
)

porc = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='porc', figure=PorcentagemTerriBrasil.buildLegalAmazon())
        ])
    ]
)

porcMun = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='porc-mun', figure=PorcentagemTerriBrasil.buildByMunDefault())
        ])
    ]
)

porcState = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='porc-state', figure=PorcentagemTerriBrasil.buildByStateDefault())
        ])
    ]
)

porcDesmMun = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='porcDesm-mun', figure=PorcentagemDesmatamento.buildByMunDefault())
        ])
    ]
)

porcDesmState = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='porcDesm-state', figure=PorcentagemDesmatamento.buildByStateDefault())
        ])
    ]
)

desm21AnosLbl = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='desm21AnosLabel', figure=Desm21AnosLabel.buildLegalAmazon())
        ])
    ]
)

desm21AnosLblMun = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='desm21AnosLabelMun', figure=Desm21AnosLabel.buildByMunDefault())
        ])
    ]
)

desm21AnosLblState = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='desm21AnosLabelState', figure=Desm21AnosLabel.buildByStateDefault())
        ])
    ]
)

totalDesmatado = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='ttDesm', figure=TotalDesmatado.buildLegalAmazon())
        ])
    ]
)

totalDesmatadoMun = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='ttDesmMun', figure=TotalDesmatado.buildByMunDefault())
        ])
    ]
)

totalDesmatadoState = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='ttDesmState', figure=TotalDesmatado.buildByStateDefault())
        ])
    ]
)

desmBarraMun = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='dbarraMun', figure=DesmBarra.buildByMunDefault())
        ])
    ]
)

desmBarraState = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='dbarraState', figure=DesmBarra.buildByStateDefault())
        ])
    ]
)

maiorAnoMun = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='maior-ano-mun', figure=MaiorAnoLabel.buildByMunDefault())
        ])
    ]
)

maiorAnoState = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='maior-ano-state', figure=MaiorAnoLabel.buildByStateDefault())
        ])
    ]
)

maiorAnoKmMun = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='maior-ano-km-mun', figure=MaiorAnoKmLabel.buildByMunDefault())
        ])
    ]
)

maiorAnoKmState = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='maior-ano-km-state', figure=MaiorAnoKmLabel.buildByStateDefault())
        ])
    ]
)

florestaRestanteMun = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='floresta-mun', figure=FlorestaRestanteLabel.buildByMunDefault())
        ])
    ]
)

florestaRestanteState = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='floresta-state', figure=FlorestaRestanteLabel.buildByStateDefault())
        ])
    ]
)

tabelaMun = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='table-mun', figure=Tabela.buildByMunDefault())
        ])
    ]
)


tabelaState = dbc.Card(
    [
        html.Div(children=[
            dcc.Graph(id='table-state', figure=Tabela.buildByStateDefault())
        ])
    ]
)



titleMun = html.H1(id="labelMun", children=Title.buildByMunDefault())
titleState = html.H1(id="labelState", children=Title.buildByStateDefault())
title = html.H1(id="labelLA", children=Title.buildLegalAmazon())

visao_geral = html.Div(children=[
    title,
    html.Div(children=[
            dbc.Row([
                dbc.Col(area, md=3),
                dbc.Col(porc, md=3),
                dbc.Col(desm21AnosLbl, md=3),
                dbc.Col(totalDesmatado, md=3)
            ]),
        ]),
        html.Div(children=[
            dbc.Row([
                dbc.Col(mapa, md=4),
                dbc.Col(mapa_arco, md=4),
                dbc.Col(florestas, md=4)
            ])
        ]),
        html.Div(children=[
            dbc.Row([
                dbc.Col(cidades, md=6),
                dbc.Col(desmatamento21anos, md=6)
            ])
        ])
    ]
)

visao_municipio = html.Div(children=[
        titleMun,
        html.Div(children=[
            dbc.Row([
                dbc.Col(area_mun, md=3),
                dbc.Col(porcMun, md=3),
                dbc.Col(totalDesmatadoMun, md=3),
                dbc.Col(porcDesmMun, md=3)
            ]),
        ]),
        html.Div(children=[
            dbc.Row([
                dbc.Col(mapa_mun, md=6),
                dbc.Col(tabelaMun, md=6)
            ]),
            dbc.Row([
                dbc.Col(desmBarraMun, md=12)],
            )
        ])
    ]
)

visao_estado = html.Div(children=[
        titleState,
        html.Div(children=[
            dbc.Row([
                dbc.Col(area_state, md=3),
                dbc.Col(porcState, md=3),
                dbc.Col(totalDesmatadoState, md=3),
                dbc.Col(porcDesmState, md=3)
            ]),
        ]),
        html.Div(children=[
            dbc.Row([
                dbc.Col(map_state, md=6),
                dbc.Col(tabelaState, md=6),
            ]),
            dbc.Row([
                dbc.Col(desmBarraState, md=12)],
            )
        ])
    ]
)


app.layout = html.Div(className="bg-light", children=[
    
    html.Div(className="grid", children=[
        html.Div(children=[
            dbc.Row([
                dbc.Col(html.H1(children='Desmatamento Amazônia Legal'), md=9),
                dbc.Col(html.Div(children=[html.Label('Visão'), dcc.Dropdown(['Geral', 'Municípios', 'Estados'], 'Geral', id="ddEscolhaDashboard"),]), md=3),
            ]),
        ]),
        html.Div(id="content"),
    ])
])

app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="make_draggable"),
    Output("drag_container", "data-drag"),
    [Input("drag_container", "id")],
)

@app.callback(
    Output("dbarraMun", "figure"),
    [Input("lam-map-mun", "clickData")]
)
def update_desmBarraMun(value):
    return DesmBarra.buildByMun(value['points'][0]['customdata'])

@app.callback(
    Output("dbarraState", "figure"),
    [Input("lam-map-state", "clickData")]
)
def update_desmBarraState(value):
    return DesmBarra.buildByState(value['points'][0]['customdata'])


@app.callback(
    Output("porc-mun", "figure"),
    [Input("lam-map-mun", "clickData")]
)
def update_porcMun(value):
    return PorcentagemTerriBrasil.buildByMun(value['points'][0]['customdata'])

@app.callback(
    Output("porc-state", "figure"),
    [Input("lam-map-state", "clickData")]
)
def update_porcState(value):
    return PorcentagemTerriBrasil.buildByState(value['points'][0]['customdata'])


@app.callback(
    Output("porcDesm-mun", "figure"),
    [Input("lam-map-mun", "clickData")]
)
def update_porcDesmMun(value):
    return PorcentagemDesmatamento.buildByMun(value['points'][0]['customdata'])

@app.callback(
    Output("porcDesm-state", "figure"),
    [Input("lam-map-state", "clickData")]
)
def update_porcDesmState(value):
    return PorcentagemDesmatamento.buildByState(value['points'][0]['customdata'])
    

@app.callback(
    Output("area-mun", "figure"),
    [Input("lam-map-mun", "clickData")]
)
def update_areaMun(value):
    return Area.buildByMun(value['points'][0]['customdata'])

@app.callback(
    Output("area-state", "figure"),
    [Input("lam-map-state", "clickData")]
)
def update_areaState(value):
    return Area.buildByState(value['points'][0]['customdata'])


@app.callback(
    Output("maior-ano-mun", "figure"),
    [Input("lam-map-mun", "clickData")]
)
def update_maiorMun(value):
    return MaiorAnoLabel.buildByMun(value['points'][0]['customdata'])

@app.callback(
    Output("maior-ano-state", "figure"),
    [Input("lam-map-state", "clickData")]
)
def update_maiorState(value):
    return MaiorAnoLabel.buildByState(value['points'][0]['customdata'])


@app.callback(
    Output("maior-ano-km-mun", "figure"),
    [Input("lam-map-mun", "clickData")]
)
def update_maiorKmMun(value):
    return MaiorAnoKmLabel.buildByMun(value['points'][0]['customdata'])

@app.callback(
    Output("maior-ano-km-state", "figure"),
    [Input("lam-map-state", "clickData")]
)
def update_maiorKmState(value):
    return MaiorAnoKmLabel.buildByState(value['points'][0]['customdata'])

@app.callback(
    Output("floresta-mun", "figure"),
    [Input("lam-map-mun", "clickData")]
)
def update_florestaMun(value):
    return FlorestaRestanteLabel.buildByMun(value['points'][0]['customdata'])

@app.callback(
    Output("floresta-state", "figure"),
    [Input("lam-map-state", "clickData")]
)
def update_florestaState(value):
    return FlorestaRestanteLabel.buildByState(value['points'][0]['customdata'])

@app.callback(
    Output("table-mun", "figure"),
    [Input("lam-map-mun", "clickData")]
)
def update_tableMun(value):
    return Tabela.buildByMun(value['points'][0]['customdata'])

@app.callback(
    Output("table-state", "figure"),
    [Input("lam-map-state", "clickData")]
)
def update_tableMun(value):
    return Tabela.buildByState(value['points'][0]['customdata'])



@app.callback(
    Output("labelMun", "children"),
    [Input("lam-map-mun", "clickData")]
)
def update_titleMun(value):
    return Title.buildByMun(value['points'][0]['customdata'])

@app.callback(
    Output("labelState", "children"),
    [Input("lam-map-state", "clickData")]
)
def update_titleState(value):
    return Title.buildByState(value['points'][0]['customdata'])

@app.callback(
    Output("ttDesmMun", "figure"),
    [Input("lam-map-mun", "clickData")]
)
def update_TotalMun(value):
    return TotalDesmatado.buildByMun(value['points'][0]['customdata'])

@app.callback(
    Output("ttDesmState", "figure"),
    [Input("lam-map-state", "clickData")]
)
def update_TotalState(value):
    return TotalDesmatado.buildByState(value['points'][0]['customdata'])

@app.callback(Output("content", "children"), [Input("ddEscolhaDashboard", "value")])
def update_dashboard(value):
    if(value == "Geral"):
        return visao_geral
    elif(value == "Municípios"):
        return visao_municipio
    elif(value == "Estados"):
        return visao_estado
    return html.H1("Erro")

if __name__=='__main__':
    app.run_server()
