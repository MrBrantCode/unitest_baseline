"""
QUESTION:
Create a function called `flatten_3D_matrix` that takes a 3D matrix as input. The function should return a dictionary containing the frequency of each numeric element in the matrix, excluding non-numeric values. The function should be able to handle non-numeric values (such as strings) without breaking.
"""

def flatten_3D_matrix(matrix):
    """
    This function takes a 3D matrix as input and returns a dictionary containing the frequency of each numeric element in the matrix, excluding non-numeric values.

    Args:
        matrix (list): A 3D matrix

    Returns:
        dict: A dictionary containing the frequency of each numeric element in the matrix
    """
    flattened = []
    for layer in matrix:
        for row in layer:
            for element in row:
                try:
                    if isinstance(element, int) or isinstance(element, float): 
                        flattened.append(element)
                except ValueError:
                    continue
    return dict((i, flattened.count(i)) for i in flattened)