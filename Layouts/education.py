import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px

########################################################################################################################


layout = html.Div([
    html.H1('Education'),
    html.H3('Formal Education'),
    html.Div([
        dcc.Markdown('''
        * **Year2** - Masters
        * **Year1** - Bachelors
        ''')
    ]),
    html.H3('Extra-Curricular Education'),
    html.Div([
        dcc.Markdown('''
    *  Really awesome extra curricular
    ''')
    ]),

])