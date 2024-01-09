#from flask import Flask, render_template
from flask import Flask, render_template,send_from_directory
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import time
#app = Flask(__name__,static_url_path='/static',static_folder='static')
app = Flask(__name__)
@app.route('/')
def index3():
# Convert the plot to base64 for embedding in HTML
# Render the HTML template with the embedded plot
	return render_template('index3.html')
@app.route('/data.txt')
def data():
	return render_template('index4.html')
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5002,debug=True)
