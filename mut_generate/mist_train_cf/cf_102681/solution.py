"""
QUESTION:
Create a function named `generate_squares_dict` that takes a positive integer `n` (where 1 <= n <= 100) as input and returns a dictionary where the keys are integers from 1 to `n` and the values are the squares of the corresponding keys.
"""

def generate_squares_dict(n):
    squares_dict = {i: i**2 for i in range(1, n+1)}
    return squares_dict