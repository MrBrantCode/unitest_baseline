"""
QUESTION:
Create a function `crescentOrderArray` that generates a 2D array with a specified number of rows and columns, where each element is a unique, incrementing integer. The function should take two parameters: `rows` and `columns`, and return a 2D list of integers. The function should be as concise as possible, ideally using a list comprehension or similar syntax.
"""

def crescentOrderArray(rows, columns):
    return [[i * columns + j + 1 for j in range(columns)] for i in range(rows)]