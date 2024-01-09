import dash
import dash_core_components as dcc
import dash_html_components as html

with open('data.txt','r') as file:
	lines = file.readlines()

data = [line.strip().split('\t') for line in lines]
headers = data[0]
numeric_data = data[1:]

x_values = [row[0] for row in numeric_data]
y1_values = [row[1] for row in numeric_data]
y2_values = [row[2] for row in numeric_data]
y3_values = [row[3] for row in numeric_data]

x_val = x_values[-10:]
y1_val = y1_values[-10:]

app = dash.Dash()

app.layout = html.Div(children =[
	html.H1("Dash Tutorial"),
	dcc.Graph(
		id ="example",
		figure ={
			'data':[
					{'x':x_val,
						'y':y1_val,
						'type':'line',
						'name':'Time-CPU'},
				],
			'layout':{
				'title':'Basic Dashboard'
			}
		}
	)
])

if __name__ == '__main__':
	app.run_server()
