import numpy as np

A = np.array([1.0, -1.0, 2.0, 1.0])
deg = 3.14/6

T = np.matrix([[1.0, 0.0, 0.0, -1.0], # Transform origin to (1, -1, -5)
                [0.0, 1.0, 0.0, 1.0],
                [0.0, 0.0, 1.0, 5.0],
                [0.0, 0.0, 0.0, 1.0]])

T1 = np.matrix([[1.0, 0.0, 0.0, 1.0], # Transform origin back
                [0.0, 1.0, 0.0, -1.0],
                [0.0, 0.0, 1.0, -5.0],
                [0.0, 0.0, 0.0, 1.0]])

R = np.matrix([[np.cos(deg), 0.0, -np.sin(deg), 0.0], # Rotation matrix around origin
                [0.0, 1.0, 0.0, 0.0],
                [np.sin(deg), 0.0, np.cos(deg), 0.0],
                [0.0, 0.0, 0.0, 1.0]])

print(T1.dot(R).dot(T).dot(A))
