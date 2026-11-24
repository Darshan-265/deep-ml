import numpy as np

def calculate_dot_product(vec1, vec2):
    """
    Calculate the dot product of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The dot product of the two vectors.
    """
    # Your code here
    arr1 = np.array(vec1)
    arr2 = np.array(vec2)

    if len(arr1)==len(arr2):
        total_sum = 0

        for i in range(len(arr1)):
            total_sum+=arr1[i]*arr2[i]
        return total_sum

    else :
        return -1


    

    
    pass