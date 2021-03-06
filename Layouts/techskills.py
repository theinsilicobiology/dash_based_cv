import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly_express as px

########################################################################################################################


layout = html.Div([
    html.H1('Tech Skills'),
    html.H4('Operating Systems'),
    html.Div([
        dcc.Markdown('''
        * Working with all the Operating Systems
         ''')
    ]),
    html.H4('Programming Languages'),
    html.Div([
        dcc.Markdown('''
        * Python
        * R
        
        ''')
    ]),
    html.H4('Databases/Big Data'),
    html.Div([
        dcc.Markdown('''
        * MySQL:
        * MongoDB
            ''')
    ]),
    html.H4('Data Visualization'),
    html.Div([
        dcc.Markdown('''
        * Dash! =)
        * Power BI
                
                ''')
    ]),





])