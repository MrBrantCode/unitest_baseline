"""
QUESTION:
Create a function named `find_value` that takes a 2D list (`matrix`) and a target value as input. The function should return a tuple containing the frequency of the target value in the matrix and a list of its index positions (as tuples of row and column indices). If the matrix is empty, the function should return 'Error: Array is empty.' If the target value is not found in the matrix, the function should return 'Error: Target value not found.'
"""

def find_value(matrix, value):
    if not any(matrix):  # check if the matrix is empty
        return 'Error: Array is empty.'

    count = 0
    positions = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == value:
                count += 1
                positions.append((i, j))

    if count == 0:
        return 'Error: Target value not found.'
    else:
        return count, positions