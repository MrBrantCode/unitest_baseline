"""
QUESTION:
Write a function called `sum_and_max_product` that takes a 2D matrix as input, calculates the sum of all elements in the matrix where each element is multiplied by its row index, and finds the maximum product among all rows. The function should return a tuple containing the sum and the maximum product. The input matrix can contain negative numbers.
"""

def sum_and_max_product(matrix):
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