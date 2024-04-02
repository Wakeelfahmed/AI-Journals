import matplotlib.pyplot as plt
import numpy as np

x = np.array([12, 11, 8, 6, 9, 6, 10])
y = np.array([4, 5, 1, 4, 3, 6, 2])
plt.bar(x, y)  # or plt.scatter(x,y)
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()
