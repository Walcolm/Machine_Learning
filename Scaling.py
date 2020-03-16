from sklearn.preprocessing import StandardScaler
import numpy as np
x = np.array([[-1,100],[0,-119],[1,512],[10,-729]])
scaler = StandardScaler()
x = scaler.fit_transform(x)
print(x)