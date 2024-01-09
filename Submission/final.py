# importing required libraries
import dash
import dash_core_components as dcc
import dash_html_components as html

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


