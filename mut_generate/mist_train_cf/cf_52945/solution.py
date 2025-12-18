"""
QUESTION:
Create a function `generate_squares` that generates a list of square values of integers from 0 up to, but not including, a given endpoint. The function should take one argument `n` representing the endpoint. The generated list should contain the squares of integers from 0 to `n-1`.
"""

def generate_squares(n):
    """Generates a list of square values of integers from 0 up to, but not including, a given endpoint."""
    return [x * x for x in range(n)]