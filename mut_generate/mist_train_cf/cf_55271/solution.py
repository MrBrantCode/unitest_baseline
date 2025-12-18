"""
QUESTION:
Create a function `sum_of_distinct_elements` that calculates the sum of the distinct elements in a four-dimensional matrix. The function should take a 4D list as input and return the sum of its distinct elements. The 4D list can contain duplicate values.
"""

def sum_of_distinct_elements(matrix):
    """
    This function calculates the sum of the distinct elements in a four-dimensional matrix.

    Args:
        matrix (list): A 4D list containing integers.

    Returns:
        int: The sum of the distinct elements in the matrix.
    """
    distinct_elements = set([i for sublist1 in matrix for sublist2 in sublist1 for sublist3 in sublist2 for i in sublist3])
    return sum(distinct_elements)