"""
QUESTION:
Create a function `sum_squares_cubes_to_n(n)` that takes an integer `n` as input and returns a tuple of three values: the sum of all integers from 1 to `n`, the sum of the squares of all integers from 1 to `n`, and the sum of the cubes of all integers from 1 to `n`. The function should be able to handle any positive integer input.
"""

def sum_squares_cubes_to_n(n: int):
    sum_n = 0
    sum_square_n = 0
    sum_cube_n = 0
    for i in range(1, n+1):
        sum_n += i
        sum_square_n += i**2
        sum_cube_n += i**3
    return (sum_n, sum_square_n, sum_cube_n)