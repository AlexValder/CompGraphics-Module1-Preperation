import numpy as np

############# Base Functions and Matrixes #############

# Scaling

def scale_matrix(k_x: float, k_y: float, k_z: float) -> np.matrix:
    return np.matrix([
        [k_x, 0.0, 0.0],
        [0.0, k_y, 0.0],
        [0.0, 0.0, k_z]
    ])

def unscale_matrix(k_x: float, k_y: float, k_z: float) -> np.matrix:
    return np.matrix([
        [1.0/k_x, 0.0, 0.0],
        [0.0, 1.0/k_y, 0.0],
        [0.0, 0.0, 1.0/k_z]
    ])

# Projection over planes

M_xy = np.matrix([
                  [1.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [0.0, 0.0, -1.0]
                ])

M_yz = np.matrix([
                  [-1.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [0.0, 0.0, 1.0]
                ])

M_xy = np.matrix([
                  [1.0, 0.0, 0.0],
                  [0.0, 1.0, 0.0],
                  [0.0, 0.0, -1.0]
                ])

# Rotation

def R_x(deg: float) -> np.matrix:
    return np.matrix([
        [1.0, 0.0, 0.0],
        [0.0, np.cos(deg), np.sin(deg)],
        [0.0, -np.sin(deg), np.cos(deg)]
    ])

def R_y(deg: float) -> np.matrix:
    return np.matrix([
        [np.cos(deg), 0.0, -np.sin(deg)],
        [0.0, 1.0, 0.0],
        [np.sin(deg), 0.0, np.cos(deg)]
    ])

def R_z(deg: float) -> np.matrix:
    return np.matrix([
        [np.cos(deg), np.sin(deg), 0.0],
        [-np.sin(deg), np.cos(deg), 0.0],
        [0.0, 0.0, 1.0]
    ])

# Movement

def T(dx: float, dy: float, dz: float) -> np.matrix:
    return np.matrix([
        [1.0, 0.0, 0.0, -dx],
        [0.0, 1.0, 0.0, -dy],
        [0.0, 0.0, 1.0, -dz],
        [0.0, 0.0, 0.0, 1.0]
    ])

def T_1(dx: float, dy: float, dz: float) -> np.matrix:
    return np.matrix([
        [1.0, 0.0, 0.0, dx],
        [0.0, 1.0, 0.0, dy],
        [0.0, 0.0, 1.0, dz],
        [0.0, 0.0, 0.0, 1.0]
    ])

############# Example Tasks #############

# Побудувати матрицю перетворення щодо обертання навколо осі, яка
# проходить через точку A(x_A, y_A, z_A). Напрямок прямої задано
# одиничним вектором (l, m, n).

# l^2 + m^2 + n^2 = 1
# Зсув системи координат в А:

(l, m, n) = (1.0, 1.0, 1.0)
(x_A, y_A, z_A) = (10.0, 10.0, 10.0)

ex_T = T(x_A, y_A, z_A)

d = np.sqrt(m**2 + n**2)

alpha = np.arccos(n/d)

ex_R_x = np.matrix([
    [1.0, 0.0, 0.0, 0.0],
    [0.0, n/d, m/d, 0.0],
    [0.0, -m/d, n/d, 0.0],
    [0.0, 0.0, 0.0, 1.0]
])

print(f"l = {l}, m = {m}, n = {n}, d = {d}")
print(f"[l, m, n, 1][R_x] = {np.array([l, m, n, 1.0] * ex_R_x)}")

ex_R_y = np.matrix([
    [d, 0.0, l, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [-l, 0.0, d, 0.0],
    [0.0, 0.0, 0.0, 1.0]
])

print(f"[l, 0, d, 1][R_y] = {np.array([0.0, 0.0, 1.0, 1.0])}")

