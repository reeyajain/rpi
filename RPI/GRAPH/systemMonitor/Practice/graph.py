import matplotlib.pyplot as plt

with open('data.txt','r') as file:
	lines = file.readlines()

data = [line.strip().split('\t') for line in lines]
headers = data[0]
numeric_data = data[1:]

x_values = [row[0] for row in numeric_data]
y1_values = [row[1] for row in numeric_data]
y2_values = [row[2] for row in numeric_data]
y3_values = [row[3] for row in numeric_data]

plt.plot(x_values,y1_values)
plt.xlabel(headers[0])
plt.ylabel(headers[1])
plt.title('Time-CPU plot')
plt.xticks(rotation=90)
plt.show()

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
figure,axis = plt.subplots(3,1)

axis[0,0].plot(x_values,y1_values)
axis[0,0].xlabel(headers[0])
axis[0,0].ylabel(headers[1])
axis[0,0].set_title('Time-CPU plot')
axis[0,0].xticks(rotation=90)

axis[0,1].plot(x_values,y2_values)
axis[0,1].xlabel(headers[0])
axis[0,1].ylabel(headers[2])
axis[0,1].set_title('Time-Memory plot')
axis[0,1].xticks(rotation=90)

axis[0,2].plot(x_values,y3_values)
axis[0,2].xlabel(headers[0])
axis[0,2].ylabel(headers[3])
axis[0,2].set_title('Time-Temperature plot')
axis[0,2].xticks(rotation=90)

plt.show()
'''
