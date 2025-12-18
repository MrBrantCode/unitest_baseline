"""
QUESTION:
Write a Python function `is_perfect_square` to loop through a multidimensional array of integers, find perfect squares, calculate their square roots, and store them in a dictionary. The function should take a multidimensional array as input, check each item to ensure it is an integer, and then verify if it is a perfect square. If it is a perfect square, calculate its square root using `math.isqrt` and store the perfect square as the key and its square root as the value in the dictionary. The function should exclude non-integer values from the final dictionary.
"""

import math

def entrance(num_array):
    # Function to check if a number is perfect square
    def is_perfect_square(n):
        return n == math.isqrt(n) ** 2

    # Initialize an empty dictionary to store perfect squares and their square roots
    perfect_squares = {}

    # Loop through the multidimensional array
    for sublist in num_array:
        for item in sublist:
            # Check if the item is integer
            if type(item) == int:
                # Check if the item is perfect square
                if is_perfect_square(item):
                    # Store the perfect square and its square root in the dictionary
                    perfect_squares[item] = math.isqrt(item)

    return perfect_squares