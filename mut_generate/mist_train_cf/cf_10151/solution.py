"""
QUESTION:
Write a function named `fill_zeros_2d_array` that takes in the number of rows and columns as parameters, and returns a 2D array of the specified size filled with zeros. The function should use a single loop to initialize and fill the array. Do not use any built-in array or matrix functions or methods.
"""

def fill_zeros_2d_array(rows, cols):
    array = []
    for i in range(rows):
        array.append([0] * cols)
    return array