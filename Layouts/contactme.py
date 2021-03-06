import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px

########################################################################################################################


layout = html.Div([
    html.H1('Contact Me'),
    html.H3('Email'),
    html.Div([
        dcc.Markdown('''
        The is how you reach me by email. 
        -  <thisismyawesomeandprofessional@email.com> 
        ''')
    ]),
    html.H3('Social Media'),
    html.Div([
        dcc.Markdown('''
        You can find me on:
    '''),
    ]),
    html.Div([
        html.Label(['LinkedIn :  ', html.A('link', href='https://www.linkedin.com/')]), #change with yours
    ]),
    html.Div([
        html.Label(['Twitter :  ', html.A('link', href='https://twitter.com/')])#change with yours
    ]),
    html.Div([
        html.Label(['Instagram :  ', html.A('link', href='https://www.instagram.com/')]) #change with yours
    ]),

])