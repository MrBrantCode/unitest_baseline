"""
QUESTION:
Create a function named `count_squares` that takes a 2D list of integers as input and returns the count of integers that are perfect squares. The function should iterate through each integer in the 2D list, check if it is a perfect square by verifying if its square root is an integer, and increment a counter for each perfect square found.
"""

import math

def count_squares(matrix):
    count = 0
    for row in matrix:
        for num in row:
            if math.sqrt(num).is_integer():
                count += 1
    return count