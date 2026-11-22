import numpy as np


def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    try:
        converted_matrix= np.array(matrix)
        updated_matrix =np.linalg.inv(converted_matrix).tolist()
        return updated_matrix
    except np.linalg.LinAlgError:
        return None

   
    
