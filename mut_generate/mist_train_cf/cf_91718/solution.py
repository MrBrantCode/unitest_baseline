"""
QUESTION:
Create a function named `cube_dictionary` that takes an integer `n` as input. The function should return a dictionary where the keys are the integers from 1 to `n` and the values are the cubes of those same integers. If `n` is not a positive integer, the function should return an empty dictionary.
"""

def cube_dictionary(n):
    if not isinstance(n, int) or n <= 0:
        return {}

    result = {}
    for i in range(1, n + 1):
        result[i] = i ** 3

    return result