import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px

########################################################################################################################


layout = html.Div([
    html.H1('Work Experience'),
    html.H3('Work'),
    html.Div([
        dcc.Markdown('''
         * **Date** - great job
            * solved many problems
         * **Date** - great job
            * solved many problems
        ''')
    ]),
    html.H3('Volunteer Work'),
    html.Div([
        dcc.Markdown('''
         * **Date** - great job
            * solved many problems
         * **Date** - great job
            * solved many problems
    ''')
    ]),

])