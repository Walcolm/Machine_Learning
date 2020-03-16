import numpy as np
from sklearn.linear_model import LinearRegression
x = np.array([[1],[2],[3]])
y =np.array([[4],[7],[10]])
model = LinearRegression().fit(x,y)
print(model.coef_)
print(model.intercept_)
xtest = np.array([[4]])
print(model.predict(xtest))