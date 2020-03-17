import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

data = np.genfromtxt("data_test_scores.csv", delimiter=",", skip_header = 1)
X = data[:,:3]
scaler.fit(X)
X = scaler.transform(X)

X = np.c_[np.ones(X.shape[0]), X]


# X has a column of ones now

# a = np.arange(3)
# print(f"a is: {a}")

# b = np.arange(12).reshape(4,3)
# print(f"b is: {b}")

# c = b.dot(a)
# print(f"c is {c}")
# exit()

y = data[:,3]

W = np.zeros(X.shape[1])

def H(W, X):
	return X.dot(W)

def J(W, X):
	return (H(W, X) - y)**2/(2*y.shape[0])

alpha = 3e-3

Cost_per_10 = []
iterations_descent = 0
converged = False
while converged == False:
	dJ = (W.T.dot(X.T).dot(X) - y.T.dot(X))/y.shape[0]
	W = W - alpha*dJ
	if np.vectorize(abs)(dJ).sum() < 0.001:
		converged = True
	iterations_descent +=1
	if iterations_descent%10 == 0:
		Cost_per_10.append(J(W, X))
Xtest = input("test numbers?").split()
Xtest = np.array(list(map(int, Xtest)))
Xtest = scaler.transform([Xtest])
Xtest = np.c_[1, Xtest]
print(H(W, Xtest))

# plt.plot(range(len(Cost_per_10)),Cost_per_10)
# plt.show()

"""

dJ/dW = (W^t)(X^T)(X) - (yT)(X))

"""