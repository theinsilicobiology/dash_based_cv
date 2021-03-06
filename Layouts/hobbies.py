import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px
import base64



########################################################################################################################


layout = html.Div([
    html.H1('Hobbies'),
    html.H3('VideoGames'),
    html.Div([
        dcc.Markdown('''
        * I love playing videogames 
        '''),

    ])

])