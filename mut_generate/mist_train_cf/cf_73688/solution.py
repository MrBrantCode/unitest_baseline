"""
QUESTION:
Create a function named `solve` that takes a three-dimensional array `matrix` as input. The function should calculate the sum of all numeric entities (integers and floating numbers) in the array, skipping non-numeric entities (such as strings) and handling any potential errors during the computation.
"""

def solve(matrix):
    """
    This function calculates the sum of all numeric entities in a three-dimensional array.
    
    Args:
        matrix (list): A 3D array containing numeric and non-numeric entities.
    
    Returns:
        float: The sum of all numeric entities in the array.
    """
    
    total = 0
    
    # Loops through each dimension of the array
    for lst_1 in matrix:
        for lst_2 in lst_1:
            for value in lst_2:
                # Error Handling
                try:
                    # Checks if the value is numerical (either integer or floating number)
                    if isinstance(value, (int, float)):
                        total += value
                except TypeError:
                    continue
                    
    return total