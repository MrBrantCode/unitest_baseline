"""
QUESTION:
Write a function `find_perfects(n)` that identifies perfect squares, perfect cubes, and numbers that are both perfect squares and perfect cubes within the range of 1 to a user-defined integer `n`. The function should return the count of unique perfect squares and perfect cubes. The input `n` must be a positive integer, and the function should handle exceptions for non-integer or negative values of `n`. Additionally, the function should measure its runtime and be able to calculate the average runtime over multiple executions.
"""

import time
import math

def find_perfects(n):
    """Function to find and count perfect squares and cubes"""
    try:
        if not isinstance(n, int) or n < 1:
            print("Please enter a valid positive integer")
            return
        
        squares = set()
        cubes = set()
        
        for i in range(1, int(math.pow(n, 1/3))+1):
            cube = i**3
            if cube <= n:
                cubes.add(cube)
                j = i
                while j*j <= n:
                    square = j*j
                    if square == cube:
                        squares.add(square)
                    j += 1

        overlap = list(squares.intersection(cubes))

        print("Count of unique perfect squares: {}".format(len(squares)))
        print("Count of unique perfect cubes: {}".format(len(cubes)))
        print("Count of numbers that are both perfect squares and perfect cubes: {}".format(len(overlap)))
        
    except Exception as e:
        print("Error occurred: ", str(e))