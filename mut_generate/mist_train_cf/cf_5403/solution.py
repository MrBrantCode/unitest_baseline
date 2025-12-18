"""
QUESTION:
Write a function `convert_to_matrix` that takes an array of numbers and a target number as input. The function should return a square matrix such that the sum of each row, column, and diagonal is equal to the target number. Additionally, the elements in the top left to bottom right diagonal must be strictly increasing in value. If no such matrix exists, the function should return `None` or indicate that no solution is found.
"""

def convert_to_matrix(arr, target):
    n = len(arr)
    size = int(n ** 0.5)
    
    if size * size != n:
        return None

    # sort the array
    arr.sort()

    # initialize the matrix
    matrix = [[0] * size for _ in range(size)]

    # populate the matrix with the elements from the array
    index = 0
    for i in range(size):
        for j in range(size):
            matrix[i][j] = arr[index]
            index += 1

    # swap the elements in the second row
    matrix[1], matrix[size - 1] = matrix[size - 1], matrix[1]

    # check if the sum of each row, column, and diagonal is equal to the target number
    for i in range(size):
        row_sum = sum(matrix[i])
        col_sum = sum(matrix[j][i] for j in range(size))
        if row_sum != target or col_sum != target:
            return None

    diagonal_sum1 = sum(matrix[i][i] for i in range(size))
    diagonal_sum2 = sum(matrix[i][size - i - 1] for i in range(size))
    if diagonal_sum1 != target or diagonal_sum2 != target:
        return None

    return matrix