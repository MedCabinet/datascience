#DataScience/MedCabinet/app.py
"""
#TODO
"""
# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

#app imports
import plotly
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pandas as pd
import os
import numpy


def create_app():
    """
    Creates the app
    """
    app = dash.Dash(__name__)

    app.layout =html.Div(dcc.Graph(id))

    # DB.init_app(app) #Makes DataBase

    @app.route('/')
    def root():
        return 

    # @app.route('/strain')
    # def strain():
    #     pass

    return app


