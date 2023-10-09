import numpy as np

#task 1542, correct
# Af = np.array([[1, 1, 3], [0, 5, -1], [2, 7, -3]])
# Tef = np.array([[1, 1, 1], [2, 1, 1], [1, 2, 0]])
# Tfe = np.linalg.inv(Tef)
# T = Tfe
# f_sopr = T @ T.T @ Af.T @ np.linalg.inv(T).T @ np.linalg.inv(T)
# print(f_sopr)

#task 1541, correct
# Af = np.array([[1, 2], [1, -1]])
# Tef = np.array([[1, 1], [0, 1]])
# Tfe = np.linalg.inv(Tef)
# T = Tfe
# f_sopr = T @ T.T @ Af.T @ np.linalg.inv(T).T @ np.linalg.inv(T)
# print(f_sopr)

#task 1556, correct
# G = np.array([[2, 2, 1], [2, 3, 1], [1, 1, 1]])
# Af = np.array([[2, 1, 1], [-1, -3, 1], [1, 2, -1]])
# Asopr = np.linalg.inv(G) @ Af.T @ G
# print(Asopr)

#task 1558, correct
# U = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 1]])
# Af = np.array([[1, 2, -3], [2, -3, 1], [3, 2, -1]])
# Asopr = np.linalg.inv(U) @ Af.T @ U
# print(Asopr)
