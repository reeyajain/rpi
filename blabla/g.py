import pygal
from flask import Flask,render_template,request,session
from flask.templating import render_template
from pygal.style import Style
import pandas 


@app.route('/bar_route')   
def bar_route():
    try:

        bar_chart = pygal.Bar()
        bar_chart.title = 'Browser usage evolution (in %)'
        bar_chart.x_labels = map(str, range(2002, 2013))
        bar_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
        bar_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
        bar_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
        bar_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
        barchart_data=bar_chart.render_data_uri()
        return render_template('barchart.html',barchart_data=barchart_data)




    except Exception:
        return "error"
