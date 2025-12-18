"""
QUESTION:
Create a function called `compute_jagged_array` that takes a 2D jagged array as input. The array contains a mix of numeric (int, float) and non-numeric entities. The function should return the total sum of all numeric entities in the array and a dictionary where the keys are the positions (row, column) of non-numeric entities and the values are the non-numeric entities themselves.
"""

def compute_jagged_array(array):
    """
    This function takes a 2D jagged array as input and returns the total sum of all numeric entities in the array 
    and a dictionary where the keys are the positions (row, column) of non-numeric entities and the values are the non-numeric entities themselves.

    Args:
        array (list): A 2D jagged array containing a mix of numeric (int, float) and non-numeric entities.

    Returns:
        tuple: A tuple containing the total sum of numeric entities and a dictionary of non-numeric entities.
    """
    total_sum = 0
    non_numeric_dict = {}
    for i, row in enumerate(array):
        for j, item in enumerate(row):
            if isinstance(item, (int, float)):
                total_sum += item
            else:
                non_numeric_dict[(i, j)] = item
    return total_sum, non_numeric_dict