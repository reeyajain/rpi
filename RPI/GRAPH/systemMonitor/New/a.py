# app.py
from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def index():
	v=[]
	x=[]
	y=[]
	z=[]
    # Create a simple plot
	with open("data.txt") as f:
		for line in f:
			list =line.split("\t")
			v.append(list[0])
			x.append(list[1])
			y.append(list[2])
			z.append(list[3])

	plt.plot(y, x)
	plt.xlabel('Cpu-axis')
	plt.ylabel('Time-axis')

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
