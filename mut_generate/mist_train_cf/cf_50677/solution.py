"""
QUESTION:
Construct a function named `find_peak_nadir` that takes a square stochastic matrix as input, where each row sums to 1. The function should return the maximum (peak) and minimum (nadir) values present in the matrix.
"""

def find_peak_nadir(matrix):
    """
    Find the maximum (peak) and minimum (nadir) values in a square stochastic matrix.

    Args:
        matrix (list of lists): A 2D list representing the stochastic matrix.

    Returns:
        tuple: A tuple containing the maximum and minimum values in the matrix.
    """
    # Flatten the matrix into a single list
    flat_list = [item for sublist in matrix for item in sublist]
    
    # Find the maximum and minimum values
    peak = max(flat_list)
    nadir = min(flat_list)
    
    return peak, nadir