import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

app = dash.Dash(__name__)

app.layout = html.Div(
	[
		dcc.Graph(id = 'graph1', animate = True),
		dcc.Graph(id = 'graph2', animate = True),
		dcc.Graph(id = 'graph3', animate = True),
		dcc.Interval(
			id = 'graph-update',
			interval = 2000,
			n_intervals = 1

		),
	]
)

@app.callback(
	[Output('graph1', 'figure'),
	Output('graph2', 'figure'),
	Output('graph3', 'figure')],
	[ Input('graph-update', 'n_intervals') ]
)

def update_graph_scatter(n):
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


	data1 = go.Scatter(x=x_val, y=y_val, mode='lines+markers', name='CPU')
	layout1 = go.Layout(height=600,width=1200,title='Time-CPU',xaxis=dict(range=[min(x_values),max(x_values)]),yaxis = dict(range = [0,100]))
	fig1 = go.Figure(data=[data1], layout=layout1)

	data2 = go.Scatter(x=x_val, y=z_val, mode='lines+markers', name='Memory')
	layout2 = go.Layout(height=600,width=1200,title='Time-Memory',xaxis=dict(range=[min(x_values),max(x_values)]),yaxis = dict(range = [0,100]))
	fig2 = go.Figure(data=[data2], layout=layout2)

	data3 = go.Scatter(x=x_val, y=q_val, mode='lines+markers', name='Temperature')
	layout3 = go.Layout(height=600,width=1200,title='Time-Temperature',xaxis=dict(range=[min(x_values),max(x_values)]),yaxis = dict(range = [min(q_values),max(q_values)]))
	fig3 = go.Figure(data=[data3], layout=layout3)

	return fig1, fig2, fig3


if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5005)
