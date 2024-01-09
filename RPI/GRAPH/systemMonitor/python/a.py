from flask import Flask,render_template
import pandas as pd
import matplotlib.pyplot as plt

app =Flask(__name__)
@app.route("/")
def display_grpah():
	data = pd.read_csv("data.txt")
	plt.figure()
	graph_data = plt.get_figure()
	return render_template("graph.html",graph_data=graph_data)

if __name__ == " __main__":
	app.run(debug=True)
