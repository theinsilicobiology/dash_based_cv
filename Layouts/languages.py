import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
import json
import pandas as pd
import numpy as np

########################################################################################################################

# input language data
df = pd.read_csv('Data/LanguageTable.csv', sep=",")

layout = html.Div([
    html.H1('Languages'),
    html.Div([
        dcc.Markdown('''
        My native language is ________. This table follows the Common European Framework of Reference for Languages.
        ''')
    ]),
    dt.DataTable(
        data=df.to_dict('records'),
        columns=[{'id': c, 'name': c} for c in df.columns],
        style_as_list_view=True,
        style_cell={'padding': '5px'},
        style_header={
            'backgroundColor': 'white',
            'fontWeight': 'bold'
        },
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['Date', 'Region']
        ],
    )
])
