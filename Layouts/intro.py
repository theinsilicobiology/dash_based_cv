import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import base64


# -- image for intro
image_filename = 'images/genericphoto.jpg'  # replace with your own photo
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

layout = html.Div([
            html.Div([
                html.H3('Hello!'),
                html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={
                    'height': '20%',
                    'width': '20%',
                    'vertical-align': 'center'
                }),
            ], style={'textAlign': 'center'},
            ),
            html.Div([
                html.Div([
                dcc.Markdown('''
                My name is Jane Doe and I love Data Science. If you wish to to Contact Me my contacts are in [Contact Me](<addlinktopage>) page where you can find my social media and email. 
                '''),
            ],  style={'textAlign': 'center'}),
        ]),
    ])
