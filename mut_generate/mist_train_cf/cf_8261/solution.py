"""
QUESTION:
Construct a function `sum_and_max_product(matrix)` that calculates the sum of all elements in a given 2D matrix where each element is multiplied by its row index and the maximum product among all rows. The function should return a tuple containing the calculated sum and the maximum product. The matrix may contain negative numbers and each row may have a different number of elements.
"""

def sum_and_max_product(matrix):
    """
    This function calculates the sum of all elements in a given 2D matrix 
    where each element is multiplied by its row index and the maximum product among all rows.
    
    Args:
        matrix (list): A 2D list of integers.
    
    Returns:
        tuple: A tuple containing the calculated sum and the maximum product.
    """
    row_sum = 0
    max_product = float('-inf')  # initialize with negative infinity

    for i in range(len(matrix)):
        row_product = 1  # initialize product for each row
        for j in range(len(matrix[i])):
            row_sum += matrix[i][j] * i  # calculate sum of elements multiplied by row index
            row_product *= matrix[i][j]  # calculate product of elements in the row

        if row_product > max_product:
            max_product = row_product  # update maximum product if necessary

    return row_sum, max_product