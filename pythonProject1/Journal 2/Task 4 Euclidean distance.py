import pandas as pd
import numpy as np

x = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print("Original Series: ")
print(x)
print(y)
print("Euclidean distance between two series: ")
print(np.linalg.norm(x - y))
