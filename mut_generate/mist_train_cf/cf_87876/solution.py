"""
QUESTION:
Create a function `cube_dictionary(n)` that takes an integer `n` as input and returns a dictionary where the keys are the integers up to `n`, and the values are the cubes of those same integers.

The function should raise a custom exception with an appropriate error message if `n` is not a positive integer or is greater than 10^6. The function should have a time complexity of O(n) and a space complexity of O(n).
"""

class CustomException(Exception):
    pass

def cube_dictionary(n):
    if not isinstance(n, int) or n <= 0:
        raise CustomException("n must be a positive integer")
    if n > 10**6:
        raise CustomException("n must be less than or equal to 10^6")

    cubes = {}
    for i in range(1, n+1):
        cubes[i] = i * i * i

    return cubes