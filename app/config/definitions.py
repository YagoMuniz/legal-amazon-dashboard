
import os

DATASET_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'datasets', 'DesmatamentoMunicipios'))
ANO_INI = 2000
ANO_FIM = 2020
MUN_GEO = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'datasets', 'al_mun.json'))
STATES_GEO = os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'datasets', 'al_states.json'))
UF = ['AC', 'AM', 'AP', 'PA', 'MT', 'MA', 'RO', 'RR', 'TO']

PRIMARY_COLOR = {"color": "rgba(102, 193, 164, 0.7)", "line": "rgba(102, 193, 164, 1.0)" }
SECONDARY_COLOR = {"color": "rgba(239, 85, 59, 0.7)", "line": "rgba(239, 85, 59, 1.0)" }
COLORS = ["rgba(102, 193, 164, 0.7)",] * 5 + ["rgba(102, 193, 164, 1.0)",] * 5 + ["rgba(239, 85, 59, 0.7)",] * 7 + ["rgba(239, 85, 59, 1.0)"] * 3

LABEL_FONT_SIZE = 25
LABEL_CARD_SIZE = 100
CARD_BARS_SIZE = 300
