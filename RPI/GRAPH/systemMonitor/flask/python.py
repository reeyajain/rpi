from flask import Flask,send_file
app = Flask(__name__)

@app.route("/home/pi/Desktop/flask/data.txt")
def display_file(filename):
	try:
		filepath="/home/pi/Desktop/flask/data.txt"
		return send_file(filepath,as_attachment=True)
	except FileNotFoundError:
		return "File not found",404
'''
def hello_world():
	return "<p>Hello, World!</p>"
'''
if __name__ == '__main__':
	app.run(debug=True)
