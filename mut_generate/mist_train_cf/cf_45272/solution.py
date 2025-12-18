"""
QUESTION:
Create a function named `generate_squares` that takes an integer `n` as input and returns a dictionary where keys are integers from 1 to `n` (inclusive) and their corresponding values are the squares of the keys represented as strings.
"""

def generate_squares(n):
    return {i: str(i**2) for i in range(1, n+1)}