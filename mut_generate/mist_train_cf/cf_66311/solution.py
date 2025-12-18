"""
QUESTION:
Create a function `square_and_cube` that takes a number as input, calculates its square and cube, and returns both values. The function should be able to handle numeric inputs only (integers or floats).
"""

def square_and_cube(number):
    square = number ** 2
    cube = number ** 3
    return (square, cube)