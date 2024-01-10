import dash 
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go

# Read data from the .txt file
file_path = 'data.txt'  # Replace 'your_file.txt' with your file path
data = pd.read_csv(file_path, delimiter='\t')  # Assuming tab-separated data

# Initialize Dash app
app = dash.Dash(__name__)

# Layout for the table and graph
app.layout = html.Div([
    html.H1('Real-Time Graph from .txt File Data'),
    html.Div([
        dcc.Graph(id='real-time-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*1000,  # in milliseconds
            n_intervals=0
        )
    ]),
    html.Div([
        html.H2('Data from .txt File displayed as Table'),
        html.Table([
            html.Thead(html.Tr([html.Th(col) for col in data.columns])),
            html.Tbody([
                html.Tr([html.Td(data.iloc[i][col]) for col in data.columns])
                for i in range(min(len(data), 10))  # Displaying only first 10 rows
            ])
        ])
    ])
])

# Callback to update the graph with real-time data
@app.callback(
    Output('real-time-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n):
    # Generate random data from a selected column for demonstration
    x = data.index
    y = data.iloc[:, 1]  # Change the column index to the one you want to plot
    
    # Create a Plotly figure
    trace = go.Scatter(x=x, y=y, mode='lines+markers', name='Real-Time Data')
    layout = go.Layout(title='Real-Time Graph from .txt File Data')
    fig = go.Figure(data=[trace], layout=layout)
    
    return fig

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
