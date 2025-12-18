"""
QUESTION:
Write a function named `fill_with_zeros` that takes a 2D jagged array as input, where each inner array can have a different length, and returns the modified array filled with zeros using a single loop and without using any built-in functions or methods. The function should iterate over each inner array and set all its elements to zero.
"""

def fill_with_zeros(array):
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = 0
    return array