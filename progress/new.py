from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import time
import random
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
plt.style.use('fivethirtyeight')

#from matplotlib.ticker import FormatStrFormatter

with open('data.txt','r') as file:
	lines = file.readlines()

	data = [line.strip().split('\t') for line in lines]
	headers = data[0]
	numeric_data = data[1:]

x_values = [row[0] for row in numeric_data]
y1_values = [float(row[1]) for row in numeric_data]
y2_values = [float(row[2]) for row in numeric_data]
y3_values = [float(row[3]) for row in numeric_data]
#print(x_values,y1_values,y2_values)
time.sleep(2)

app = Flask(__name__)

@app.route('/p1')
def index():




	def animate(i):

		with open('data.txt','r') as file:
			lines = file.readlines()
		data = [line.strip().split('\t') for line in lines]
		numeric_data = data[1:]
		x_values = [row[0][11:19] for row in numeric_data]
		y_values = [float(row[1]) for row in numeric_data]
		x_val = x_values[-10:]
		y_val = y_values[-10:]
		plt.cla()
		plt.plot(x_val,y_val)
		plt.xticks(rotation = 90)
		plt.xlabel("Time")
		plt.ylabel("CPU Usage")
		plt.title('Time-CPU Usage')
		time.sleep(0.25)
		x_val.pop(0)
		y_val.pop(0)
	fig,axis=plt.subplots()
	ani = FuncAnimation(plt.gcf(), animate, 1000)
	plt.tight_layout()
#	plt.show()

    # Save the plot to a BytesIO object
	img_buf = BytesIO()
	plt.savefig(img_buf, format='png')
	img_buf.seek(0)
	plt.close()
    # Convert the plot to base64 for embedding in HTML
	img_data = base64.b64encode(img_buf.read()).decode('utf-8')
    # Render the HTML template with the embedded plot
	return render_template('index.html', img_data=img_data)



@app.route('/p2')
def index1():


	def animate(i):

		with open('data.txt','r') as file:
			lines = file.readlines()
		data = [line.strip().split('\t') for line in lines]
		numeric_data = data[1:]
		x_values = [row[0][11:19] for row in numeric_data]
		y_values = [float(row[2]) for row in numeric_data]
		x_val = x_values[-10:]
		y_val = y_values[-10:]
		plt.cla()
		plt.plot(x_val,y_val)
		plt.xticks(rotation = 90)
		plt.xlabel("Time")
		plt.ylabel("Memory")
		plt.title('Time-Memory')
		time.sleep(0.25)
		x_val.pop(0)
		y_val.pop(0)
	fig,axis=plt.subplots()
	ani = FuncAnimation(plt.gcf(), animate, 1000)
	plt.tight_layout()
	plt.show()

    # Save the plot to a BytesIO object
	img_buf = BytesIO()
	plt.savefig(img_buf, format='png')
	img_buf.seek(0)
	plt.close()
    # Convert the plot to base64 for embedding in HTML
	img_data = base64.b64encode(img_buf.read()).decode('utf-8')
    # Render the HTML template with the embedded plot
	return render_template('index1.html', img_data=img_data)


@app.route('/p3')
def index2():


	def animate(i):

		with open('data.txt','r') as file:
			lines = file.readlines()
		data = [line.strip().split('\t') for line in lines]
		numeric_data = data[1:]
		x_values = [row[0][11:19] for row in numeric_data]
		y_values = [float(row[3]) for row in numeric_data]
		x_val = x_values[-10:]
		y_val = y_values[-10:]
		plt.cla()
		plt.plot(x_val,y_val)
		plt.xticks(rotation = 90)
		plt.xlabel("Time")
		plt.ylabel("Temperature")
		plt.title('Time-Temperature')
		time.sleep(0.25)
		x_val.pop(0)
		y_val.pop(0)
	fig,axis=plt.subplots()
	ani = FuncAnimation(plt.gcf(), animate, 1000)
	plt.tight_layout()
	plt.show()

    # Save the plot to a BytesIO object
	img_buf = BytesIO()
	plt.savefig(img_buf, format='png')
	img_buf.seek(0)
	plt.close()
    # Convert the plot to base64 for embedding in HTML
	img_data = base64.b64encode(img_buf.read()).decode('utf-8')
    # Render the HTML template with the embedded plot
	return render_template('index2.html', img_data=img_data)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

