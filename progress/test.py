# app.py
from flask import Flask, render_template
import matplotlib.pyplot as plt
from io import BytesIO
import base64


x_values = [1,2,3,6,4,7,8,0,5,1]
y1_values = [7,3,5,1,4,2,8,9,5,2]
#y2_values = [row[2] for row in numeric_data]
#y3_values = [row[3] for row in numeric_data]

app = Flask(__name__)

@app.route('/p1')
def index():
	plt.plot(sorted(x_values),sorted(y1_values))
	plt.xlabel("x_values")
	plt.ylabel("y_values")
	plt.title('Test plot')
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
'''@app.route('/p2')
def index1():
	plt.plot(x_values,y2_values)
	plt.xlabel(headers[0])
	plt.ylabel(headers[2])
	plt.title('Time-Memory plot')
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
	return render_template('index1.html', img_data=img_data)
@app.route('/p3')
def index2():
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
	return render_template('index2.html', img_data=img_data)
'''
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
