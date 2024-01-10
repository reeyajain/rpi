import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import random
import datetime

app = dash.Dash(_name_)

# Read the .txt file into a pandas DataFrame
data = pd.read_csv('your_file.txt', delimiter='\t')  # Adjust delimiter as needed

# Create a layout with a table and multiple graphs
app.layout = html.Div([
    html.H1('Real-Time Graphs and Table'),

    html.Div([
        dcc.Graph(id='graph1'),
        dcc.Graph(id='graph2')
    ], style={'display': 'flex'}),

    html.Div([
        dcc.Interval(
            id='interval-component',
            interval=1*1000,  # in milliseconds
            n_intervals=0
        ),
        html.Table([
            html.Thead(html.Tr([html.Th(col) for col in data.columns])),
            html.Tbody([
                html.Tr([
                    html.Td(data.iloc[i][col]) for col in data.columns
                ]) for i in range(min(len(data), 10))  # Displaying first 10 rows
            ])
        ])
    ])
])

# Callback to update the multiple graphs
@app.callback(
    [Output('graph1', 'figure'),
     Output('graph2', 'figure')],
    [Input('interval-component', 'n_intervals')]
)
def update_graphs(n):
    # Generate random data for demonstration purposes
    x = datetime.datetime.now()
    y1 = random.random() * 100
    y2 = random.random() * 100

    # Create plotly figures for graph1 and graph2
    data1 = go.Scatter(x=[x], y=[y1], mode='lines+markers', name='Random Data 1')
    layout1 = go.Layout(title='Real-Time Graph 1')
    fig1 = go.Figure(data=[data1], layout=layout1)

    data2 = go.Scatter(x=[x], y=[y2], mode='lines+markers', name='Random Data 2')
    layout2 = go.Layout(title='Real-Time Graph 2')
    fig2 = go.Figure(data=[data2], layout=layout2)

    return fig1, fig2

if _name_ == '_main_':
    app.run_server(debug=True)
