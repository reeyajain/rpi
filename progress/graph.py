import matplotlib.pyplot as plt
import time

with open('data.txt','r') as file:
	lines = file.readlines()

data = [line.strip().split('\t') for line in lines]
headers = data[0]
numeric_data = data[1:]

x_values = [row[0] for row in numeric_data]
print(x_values)
y1_values = [row[1] for row in numeric_data]
y2_values = [row[2] for row in numeric_data]
y3_values = [row[3] for row in numeric_data]

plt.plot(x_values,y1_values)
plt.xlabel(headers[0])
plt.ylabel(headers[1])
plt.title('Time-CPU plot')
plt.xticks(rotation=90)
plt.show()
time.sleep(2)
'''
plt.plot(x_values,y2_values)
plt.xlabel(headers[0])
plt.ylabel(headers[2])
plt.title('Time-Memory plot')
plt.xticks(rotation=90)
plt.show()

plt.plot(x_values,y3_values)
plt.xlabel(headers[0])
plt.ylabel(headers[3])
plt.title('Time-Temperature plot')
plt.xticks(rotation=90)
plt.show()
'''

