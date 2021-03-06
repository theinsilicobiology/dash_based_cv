import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px
import base64




########################################################################################################################


layout = html.Div([
    html.H1('Soft Skills'),
    html.Div([
        dcc.Markdown('''
        * Very cool:
        * Love Data Science 
        '''),

    ]),



])