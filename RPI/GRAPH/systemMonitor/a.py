# app.py
from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
	'''time=[]
	cpu=[]
	mem=[]
	temp=[]'''
    # Create a simple plot
	with open('data.txt','r') as file:
		lines = file.readlines()

		data = [line.strip().split('\t') for line in lines]
		headers = data[0]
		numeric_data = data[1:]

		x_values = [row[0] for row in numeric_data]
		y1_values = [row[1] for row in numeric_data]
		y2_values = [row[2] for row in numeric_data]
		y3_values = [row[3] for row in numeric_data]


	'''with open("data.txt") as f:
		for line in f:
			list =line.split("\t")
			time.append(list[0][11:19])
			cpu.append(list[1])
			mem.append(list[2])
			temp.append(list[3])

	plt.plot(time,cpu)
	plt.xlabel('time-axis')
	plt.ylabel('CPU-axis')
	plt.plot(time,mem)
	plt.xlabel('time-axis')
	plt.ylabel('memory-axis')
	plt.plot(time,temp)
	plt.xlabel('time-axis')
	plt.ylabel('Temperature-axis')
	'''
	plt.plot(x_values,y1_values)
	plt.xlabel(headers[0])
	plt.ylabel(headers[1])
	plt.title('Time-CPU plot')
	plt.xticks(rotation=90)
	plt.show()

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
    # Save the plot to a BytesIO object
	img_buf = BytesIO()
	plt.savefig(img_buf, format='png')
	img_buf.seek(0)
	plt.close()

    # Convert the plot to base64 for embedding in HTML
	img_data = base64.b64encode(img_buf.read()).decode('utf-8')

    # Render the HTML template with the embedded plot
	return render_template('index.html', img_data=img_data)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
import matplotlib.pyplot as plt

