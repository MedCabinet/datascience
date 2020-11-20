from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load
import numpy as np
import pandas as pd

from app import app

Stain_use = ['Pain',
                 'Chemo',
                 'Anxiety',
                 'Seizures',
                 'Stess',
                 'Eating disorder',
                 'Insomnia',
                 'Harmful Medication withdrawal'
                 ]

style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Predict Marijana strain given use cases

    """), 

    html.Div([
        dcc.Markdown('###### Uses case'), 
        dcc.Dropdown(
            options =[ 
                {'label': 'Pain', 
                        'value': 'Pain'},
                {'lavel': 'Chemo', 
                        'value': 'Chemo'},
                {'label': 'Anxiety', 
                        'value': 'Anxiety'},
                {'lavel': 'Seizures', 
                        'value': 'Seizures'},
                {'label': 'Stress', 
                        'value': 'Stress'},
                {'lavel': 'Eating disorder', 
                        'value': 'Eating disorder'},
                {'label': 'Insomnia', 
                        'value': 'Insomnia'},
                {'lavel': 'Harmful Medication withdrawal',
                        'value': 'Harmful medIcation withrawal'},
                {'label': 'Addiction recovery', 
                        'value': 'Addiction recovary'}
            ],
            multiple=True
            ), 
    ], style=style), 

    html.Div([
        dcc.Markdown('###### Pain Index'), 
        dcc.RangeSlider(
           marks = {yin: f'Label{yin}' for yin in range(0, 11)},
           min = 0,
           max = 10,
           value= [-3, 4]
        ),
    ], style=style), 

    dcc.Markdown('### Prediction'), 
    html.Div(id='prediction-content', style={'marginBottom': '5em'}), 

])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('annual-income', 'value'),
     Input('credit-score', 'value'),
     Input('loan-amount', 'value'),
     Input('loan-purpose', 'value'),
     Input('monthly-debts', 'value')])
def predict(annual_income, credit_score, loan_amount, loan_purpose, monthly_debts):

    df = pd.read_csv('model/Cannabis_Strain_Features.csv')

    pipeline = load('model/pipeline.joblib')
    y_pred_log = pipeline.predict(df)
    y_pred = np.expm1(y_pred_log)[0]

    return f'Mstrain : {y_pred:.2f}%'
