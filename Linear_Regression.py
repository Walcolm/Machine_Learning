import matplotlib.pyplot as plt
import numpy as np


data = np.genfromtxt("data.csv", delimiter=",")
og_x_list = list(data[1:, 0])

x_list = og_x_list[:]
y_list = list(data[1:, 1])
og_y_list = list(data[:])
x_scale = (sum(x_list) / (len(x_list), max(x_list) - min(x_list)))
for i in range(len(x_list)):
    x_list[i] = (x_list[i] - x_scale[0]) / x_scale[1]
    y_list[i] = (y_list[i] - x_scale[0]) / x_scale[1]

def h(h0, h1, x):
    return h0 + h1 * x


def find_cost(h0, h1, x_list, y_list):
    error = 0
    for i in range(len(x_list)):
        hypothesis = h1 * (x_list[i]) + h_0
        error += ((hypothesis - y_list[i])**2) / (2 * len(x_list))
    return error


def partial_der_h0(h0, h1, x_list, y_list):
    partial = 0
    for i in range(len(x_list)):
        hypothesis = h1 * (x_list[i]) + h0
        partial += ((hypothesis - y_list[i])) / (len(x_list))
    return partial


def partial_der_h1(h0, h1, x_list, y_list):
    partial = 0
    for i in range(len(x_list)):
        hypothesis = h1 * (x_list[i]) + h0
        partial += ((hypothesis - y_list[i])) * (x_list[i]) / (len(x_list))
    return partial
# def a_gradiant_descent(a,h0,h1,x_list,y_list):
    # new_h0 = h0 - a*partial_der_h0(h0,h1,x_list,y_list)
    # new_h1 = h1 - a*partial_der_h1(h0,h1,x_list,y_list)
    # return [new_h0, new_h1]
converged = False
h0, h1 = 0, 0
a = 0.003
i = 0
while not converged:
    # for i in range(100):
    h0_partial = partial_der_h0(h0, h1, x_list, y_list)
    h1_partial = partial_der_h1(h0, h1, x_list, y_list)
    h0 = h0 - a * h0_partial
    h1 = h1 - a * h1_partial
    converged = abs(h0_partial) + abs(h1_partial) < 0.0001

# test_x = int(input("Testing x: "))
# test_x = (test_x - x_scale[0]) / x_scale[1]
# print("My guess for y is: " + str(h0 + h1 * test_x))

plt.plot(og_x_list, y_list, 'ro')
plt.plot([600, 900], [h(h0, h1, 600),
                    h(h0, h1, 900)])
plt.plot(og_x_list,og_y_list, 'ro')
plt.show()
