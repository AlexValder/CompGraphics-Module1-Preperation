import numpy as np

deg = 3.14

T = np.matrix([[1.0, 0.0, -4.0], # Transform origin to (4; -3)
                [0.0, 1.0, 3.0],
                [0.0, 0.0, 1.0]])

T1 = np.matrix([[1.0, 0.0, 4.0], # Transform origin back
                [0.0, 1.0, -3.0],
                [0.0, 0.0, 1.0]])

R = np.matrix([[np.cos(deg), -np.sin(deg), 0.0], # Rotate around new origin
                [np.sin(deg), np.cos(deg), 0.0],
                [0.0, 0.0, 1.0]])

A = np.array([7.0, -2.0, 1.0])
B = np.array([-1.0, 2.0, 1.0])


print(T1.dot(R).dot(T).dot(A))
print(T1.dot(R).dot(T).dot(B))