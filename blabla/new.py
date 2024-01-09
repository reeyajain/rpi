import matplotlib.pyplot as plt
import time

while True:
	with open('data.txt','r') as file:
		lines = file.readlines()

	data = [line.strip().split('\t') for line in lines]
	headers = data[0]
	numeric_data = data[1:]

	x_values = [row[0] for row in numeric_data]
	y1_values = [row[1] for row in numeric_data]
	y2_values = [row[2] for row in numeric_data]
	y3_values = [row[3] for row in numeric_data]

	plt.plot(x_values,y1_values)
	plt.xlabel(headers[0])
	plt.ylabel(headers[1])
	plt.title('Time-CPU plot')
	plt.xticks(rotation=90)
	plt.show()
	time.sleep(2)
'''
	plt.plot(x_values,y2_values)
	plt.xlabel(headers[0])
	plt.ylabel(headers[2])
	plt.title('Time-Memory plot')
	plt.xticks(rotation=90)
	plt.show()

	plt.plot(x_values,y3_values)
	plt.xlabel(headers[0])
	plt.ylabel(headers[3])
	plt.title('Time-Temperature plot')
	plt.xticks(rotation=90)
	plt.show()
'''

import dash
import dash_html_components as html
import dash_core_components as dcc
import numpy as np

from dash.dependencies import Input, Output

# Example data (a circle).
resolution = 20
t = np.linspace(0, np.pi * 2, resolution)
x, y = np.cos(t), np.sin(t)
# Example app.
figure = dict(data=[{'x': [], 'y': []}], layout=dict(xaxis=dict(range=[-1, 1]), yaxis=dict(range=[-1, 1])))
app = dash.Dash(__name__, update_title=None)  # remove "Updating..." from title
app.layout = html.Div([dcc.Graph(id='graph', figure=figure), dcc.Interval(id="interval")])


@app.callback(Output('graph', 'extendData'), [Input('interval', 'n_intervals')])
def update_data(n_intervals):
    index = n_intervals % resolution
    # tuple is (dict of new data, target trace index, number of points to keep)
    return dict(x=[[x[index]]], y=[[y[index]]]), [0], 10


if __name__ == '__main__':
    app.run_server()
