import numpy as np

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

    np_matrix = np.array(matrix)
    scaled_matrix = (np_matrix * scalar).tolist()

    return scaled_matrix



   


    pass