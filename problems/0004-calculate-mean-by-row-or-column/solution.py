import numpy as np

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:

    updated_matrix = np.array(matrix)

    if mode == 'row':
        return updated_matrix.mean(axis=1).tolist()

    if mode == 'column':
        return updated_matrix.mean(axis=0).tolist()
    
    else:
        raise ValueError("either row or column")


    