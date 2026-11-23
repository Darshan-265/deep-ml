import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    diagon = np.diag(A)
    efc = A - np.diagflat(diagon)

    x = np.zeros(len(b))

    for i in range(n):
        x = (b - np.dot(efc,x))/diagon

    return np.round(x,4).tolist()