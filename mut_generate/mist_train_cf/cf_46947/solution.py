"""
QUESTION:
Write a function `calculate_total` that takes a three-dimensional array as input and returns the total of all numeric entities within the array. The function should handle non-numeric entities by ignoring them.
"""

def calculate_total(matrix):
    """
    This function calculates the total of all numeric entities within a 3D array.

    Args:
        matrix (list): A 3-dimensional list containing numeric and non-numeric entities.

    Returns:
        int: The total of all numeric entities within the array.
    """

    total = 0
    for i in matrix:
        for j in i:
            for k in j:
                try:
                    # try to convert the entities into numeric
                    total += int(k)
                except ValueError:
                    # if can't convert into numeric then skip the entity
                    pass
    return total