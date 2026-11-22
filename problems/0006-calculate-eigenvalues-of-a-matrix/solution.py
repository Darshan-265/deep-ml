import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    all_matrix= np.array(matrix)
    find_solutiion = np.linalg.eigvals(all_matrix).real.tolist()
    return find_solutiion
    
   


 