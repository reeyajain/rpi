#from flask import Flask, render_template
from flask import Flask, render_template,send_file
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import time
#app = Flask(__name__,static_url_path='/static',static_folder='static')
app = Flask(__name__)
@app.route('/')
def index():
# Convert the plot to base64 for embedding in HTML
# Render the HTML template with the embedded plot
	return render_template('index.html')
@app.route('/rpi.jpg')
def get_image():
	return send_file('rpi.jpg',mimetype='image/jpg')
@app.route('/cpu')
def index_cpu():
# Convert the plot to base64 for embedding in HTML
# Render the HTML template with the embedded plot
	return render_template('index_cpu.html')
@app.route('/mem')
def index_mem():
# Convert the plot to base64 for embedding in HTML
# Render the HTML template with the embedded plot
	return render_template('index_mem.html')
@app.route('/temp')
def index_temp():
# Convert the plot to base64 for embedding in HTML
# Render the HTML template with the embedded plot
	return render_template('index_temp.html')
@app.route('/data.txt')
def data_file():
	return send_file("data.txt",as_attachment=True)

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5009,debug=True)
