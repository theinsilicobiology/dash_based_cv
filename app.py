# **********************************************************************
# Project           : dash_based_cv
#
# Program name      : app
#
# Author            : Susana Paço
#
# Date created      : 20210306
#
# Summary           : a basic template for a dash based curriculum
#
#
# Revision History  :
#
# Date        Author      Num    Summary
# 20210306    Susana      1      first prototype
#
#
# **********************************************************************

import os
import flask
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html


#internal structure
from dash.dependencies import Input, Output
from Layouts import  intro, education,workexperience, techskills, languages, softskills, hobbies, contactme


server = flask.Flask(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], server=server)
app.title = "Jane Doe - Awesome Data Scientist"
app.config.suppress_callback_exceptions = True

#server = app.server


# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Jane Doe", className="display-4"), # change to your name
        html.Hr(),
        html.P(
            "Awesome Data Scientist", className="lead" #change to your position
        ),
        dbc.Nav(
            [
                dbc.NavLink("Intro", href="/intro", id="intro-link"),
                dbc.NavLink("Education", href="/education", id="education-link"),
                dbc.NavLink("Work Experience", href="/workexperience", id="workexperience-link"),
                dbc.NavLink("Tech Skills", href="/techskills", id="techskills-link"),
                dbc.NavLink("Languages", href="/languages", id="languages-link"),
                dbc.NavLink("Soft Skills", href="/softskills", id="softskills-link"),
                dbc.NavLink("Hobbies", href="/hobbies", id="hobbies-link"),
                dbc.NavLink("Contact Me", href="/contactme", id="contactme-link"),

            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])




@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname in ["/", "/intro"]:
        return intro.layout
    elif pathname == "/education":
        return education.layout
    elif pathname == "/workexperience":
        return workexperience.layout
    elif pathname == "/techskills":
        return techskills.layout
    elif pathname == "/languages":
        return languages.layout
    elif pathname == "/softskills":
        return softskills.layout
    elif pathname == "/hobbies":
        return hobbies.layout
    elif pathname == "/contactme":
        return contactme.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
# ------------------ init the server ----------
if __name__ == '__main__':
    app.run_server(debug=True)
