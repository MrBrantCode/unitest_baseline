"""
QUESTION:
Write a function named `sum_and_large_elements` that takes a multidimensional matrix and a value X as input, and returns the total sum of all elements in the matrix and the indices of elements greater than X. The function should work for matrices of any dimension.
"""

def sum_and_large_elements(matrix, x):
    total_sum = 0
    indices = []

    for index, value in np.ndenumerate(matrix):
        total_sum += value
        if value > x:
            indices.append(index)

    return total_sum, indices