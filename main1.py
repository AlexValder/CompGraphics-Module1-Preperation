import numpy as np

p1 = np.array([-4.0, 22.0, 1.0])
p2 = np.array([-11.0, -6.0, 1.0])

T = np.matrix([[1.0, 0.0, 17.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0]])

M = np.matrix([[-1.0, 0.0, 0.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0]])

T1 = np.matrix([[1.0, 0.0, -17.0],
                [0.0, 1.0, 0.0],
                [0.0, 0.0, 1.0]])

print(f"P1 = {p1}", f"P2 = {p2}", f"T*M*T1*P1 = {T1.dot(M).dot(T).dot(p1)}", f"T*M*T1*P2 = {T1.dot(M).dot(T).dot(p2)}", sep='\n\n')
print(f"ANSWER = {p1[0]} {p1[1]} {p2[0]} {p2[1]}")