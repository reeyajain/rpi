from flask import Flask, Response 
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

app = Flask(__name__)

@app.route('/hi')
def index():
    return '<h1>Matplotlib Animation on Server</h1>'

def generate_animation():
    fig, ax = plt.subplots()
    x_data = np.arange(0, 2*np.pi, 0.1)
    line, = ax.plot([], [])

    def update(frame):
        y_data = np.sin(frame)
        line.set_data(x_data, y_data)
        return line,

    animation = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), interval=50, blit=True)
    
    plt.close(fig)  # Prevents the figure from displaying

    while True:
        plt.pause(0.05)
        fig.canvas.draw()
        img = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
        yield (b'--frame\r\n'
               b'Content-Type: image/png\r\n\r\n' + img.tobytes() + b'\r\n')

@app.route('/animate')
def animate():
    return Response(generate_animation(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
