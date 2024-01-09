import random
from itertools import count
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits import mplot3d
plt.style.use('fivethirtyeight')


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
		plt.xlabel("Time")
	axis[0].set_ylabel("CPU Usage")
	axis[1].set_ylabel("Memory")
	axis[2].set_ylabel("Temperature")
	axis[0].set_title('Time-CPU Usage')
	axis[1].set_title('Time-Memory')
	axis[2].set_title('Time-Temperature')
	time.sleep(0.25)
	x_val.pop(0)
	z_val.pop(0)
	y_val.pop(0)
	q_val.pop(0)
fig,axis=plt.subplots(1,3)
#area=pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d']
#area.plot(kind='area',ax=ax)
#plt.title('Demo graph for Area plot')
#plt.show()
ani = FuncAnimation(plt.gcf(), animate, 1000)
plt.tight_layout()
plt.show()
