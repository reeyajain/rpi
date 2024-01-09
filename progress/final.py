from flask import Flask, render_template
import random
from io import BytesIO
import base64
from itertools import count
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
plt.style.use('fivethirtyeight')
fig,axis=plt.subplots(1,3)

def animate(i):

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

	axis[0].cla()
	axis[0].plot(x_val,y_val)
	axis[1].cla()
	axis[1].plot(x_val,z_val)
	axis[2].cla()
	axis[2].plot(x_val,q_val)
	for ax in axis.flatten():
		plt.sca(ax)
		plt.xticks(rotation = 90)
		plt.xlabel('Time')
	axis[0].set_ylabel('CPU Usage')
	axis[1].set_ylabel('Memory')
	axis[2].set_ylabel('Temperature')
	axis[0].set_title('Time-CPU Usage')
	axis[1].set_title('Time-Memory')
	axis[2].set_title('Time-Temperature')
	time.sleep(0.25)
	x_val.pop(0)
	z_val.pop(0)
	y_val.pop(0)
	q_val.pop(0)

app = Flask(__name__)

@app.route('/')
def index():

	anim = FuncAnimation(fig, animate, 1000)
#	fig.save('live_plot.png')
#	plt.tight_layout()
#	plt.show()
# 	Save the plot to a BytesIO object
#	img_buf = BytesIO()
#	plt.savefig(img_buf, format='png')
#	img_buf.seek(0)
#	plt.close()
# 	Convert the plot to base64 for embedding in HTML
#	img_data = base64.b64encode(img_buf.read()).decode('utf-8')
#	 Render the HTML template with the embedded plot
	return render_template('index.html', img_data='live_plot.png')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

'''
# app.py
from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import time
#from matplotlib.ticker import FormatStrFormatter

while True:
	with open('data.txt','r') as file:
		lines = file.readlines()

		data = [line.strip().split('\t') for line in lines]
		headers = data[0]
		numeric_data = data[1:]

	x_values = [row[0] for row in numeric_data]
	y1_values = [float(row[1]) for row in numeric_data]
	y2_values = [float(row[2]) for row in numeric_data]
	y3_values = [float(row[3]) for row in numeric_data]
	print(x_values,y1_values,y2_values)
	time.sleep(2)

	app = Flask(__name__)

	@app.route('/p1')
	def index():
		plt.plot(x_values,sorted(y1_values))
		plt.xlabel(headers[0])
		plt.ylabel(headers[1])
		plt.title('Time-CPU plot')
		plt.xticks(rotation=90)
	#	plt.yaxis.set_major_formatter(FormatStrFormatter('%.4f'))
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
	@app.route('/p2')
	def index1():
		plt.plot(x_values,y2_values)
		plt.xlabel(headers[0])
		plt.ylabel(headers[2])
		plt.title('Time-Memory plot')
		plt.xticks(rotation=90)
	#	plt.yaxis.set_major_formatter(FormatStrFormatter('%.4f'))
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
		plt.plot(x_values,y3_values)
		plt.xlabel(headers[0])
		plt.ylabel(headers[3])
		plt.title('Time-Temperature plot')
		plt.xticks(rotation=90)
	#	plt.yaxis.set_major_formatter(FormatStrFormatter('%.4f'))
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
'''
