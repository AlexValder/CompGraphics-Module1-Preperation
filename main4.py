import numpy as np

K = np.array([-10.3, -3.0, 1.0]) # Original triangle
L = np.array([12.0, -4.0, 1.0])
M = np.array([11.0, 10.0, 1.0])

K1 = np.array([ -2.0, -8.0, 1.0]) # Image triangle
L1 = np.array([ -5.0, 4.0, 1.0])
M1 = np.array([ -2.0, 1.0, 1.0])

MA1 = np.matrix([K, L, M])
MA2 = np.matrix([K1, L1, M1])

print(np.linalg.inv(MA1))
print(MA2)

res = np.linalg.inv(MA1).dot(MA2)
print(res)
print(1.2e-1, -1.8e-1, 1e0)
