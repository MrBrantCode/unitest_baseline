"""
QUESTION:
Create a function called `find_even_numbers` that takes a 2D matrix of size 1 x 1 to 100 x 100 as input. The function should return a list of tuples, where each tuple contains an even number from the matrix and its corresponding position (row, column).
"""

def find_even_numbers(matrix):
    even_numbers = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] % 2 == 0:
                even_numbers.append((matrix[i][j], i, j))
    return even_numbers