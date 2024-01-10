import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import random
import datetime

app = dash.Dash(__name__)

# Callback to update the multiple graphs
@app.callback(
	[Output('graph1', 'figure'),
	Output('graph2', 'figure'),
	Output('graph3', 'figure')],
	[Input('interval-component', 'n_intervals')]
)
def update_graphs(n):

	with open('data.txt','r') as file:
		lines = file.readlines()
	data = [line.strip().split('\t') for line in lines]
	numeric_data = data[1:]
	x_values = [row[0][11:19] for row in numeric_data]
	y_values = [float(row[1]) for row in numeric_data]
	z_values = [float(row[2]) for row in numeric_data]
	q_values = [float(row[3]) for row in numeric_data]
	x_val = x_values[-10:]
	y_val = y_values[-10:]
	z_val = z_values[-10:]
	q_val = q_values[-10:]
	# Create plotly figures for graphs
	data1 = go.Scatter(x=x_val, y=y_val, mode='lines+markers', name='CPU')
	layout1 = go.Layout(title='Time-CPU')
	fig1 = go.Figure(data=[data1], layout=layout1)

	data2 = go.Scatter(x=x_val, y=z_val, mode='lines+markers', name='Memory')
	layout2 = go.Layout(title='Time-Memory')
	fig2 = go.Figure(data=[data2], layout=layout2)

	data3 = go.Scatter(x=x_val, y=q_val, mode='lines+markers', name='Temperature')
	layout3 = go.Layout(title='Time-Temperature')
	fig3 = go.Figure(data=[data3], layout=layout3)

	return fig1, fig2, fig3

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5005)
