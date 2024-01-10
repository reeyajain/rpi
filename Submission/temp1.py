import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
'''
x_val = deque(maxlen = 20)
x_val.append(1)

z_val = deque(maxlen = 20)
z_val.append(1)
'''
app = dash.Dash(__name__)

app.layout = html.Div(
	[
		dcc.Graph(id = 'live-graph', animate = True),
		dcc.Interval(
			id = 'graph-update',
			interval = 5000,
			n_intervals = 1

		),
	]
)

@app.callback(
	Output('live-graph', 'figure'),
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

#	X.append(X[-1]+1)
#	Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))

	data = plotly.graph_objs.Scatter(
			x=x_val,
			y=z_val,
			name='Memory',
			mode= 'lines+markers'
	)

	return {'data': [data],
			'layout' : go.Layout(xaxis=dict(range=[min(x_val),max(x_val)]),yaxis = dict(range = [min(z_val),max(z_val)]),)}

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5005)
