import matplotlib.pyplot as plt
import numpy as np


data = np.genfromtxt("data.csv",delimiter=",")
x_list = list(data[1:, 0])
y_list = list(data[1:, 1])
# have same length
plt.plot(x_list, y_list, 'ro')
plt.plot([500, 800], [195,273])
plt.show()
#h0 ~ 65
def find_cost(h_1, x_list, y_list):
	error = 0
	for i in range(len(x_list)):
		hypothesis = h_1 * (x_list[i]) + 65
		error += ((hypothesis - y_list[i])**2)/(2* len(x_list))
	return error
def cost(x_list, y_list):
	list_of_errors = []
	for i in range(20,32):
		list_of_errors.append(find_cost(i/100, x_list, y_list))
	return list_of_errors

# plt.plot([i for i in range(20, 32)], cost(x_list,y_list), 'ro')
# plt.show()
