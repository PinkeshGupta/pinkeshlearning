import numpy as np
store = np.array([0, 9, 0, 1])
cost  = np.array([82, 82, 73, 73])
np_cols = np.column_stack((store, cost))

print(np_cols)
