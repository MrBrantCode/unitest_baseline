"""
QUESTION:
Create a function named `create_squared_dict(n)` that generates a dictionary containing numbers up to `n` as keys and their squares as values, excluding perfect squares. The function should also return the sum of all the squares in the dictionary. The input `n` is a positive integer, and the function should iterate from 1 to `n` (inclusive) to generate the dictionary and sum of squares.
"""

def create_squared_dict(n):
    """
    Generate a dictionary containing numbers up to `n` as keys and their squares as values, 
    excluding perfect squares, and return the sum of all the squares in the dictionary.

    Args:
        n (int): A positive integer.

    Returns:
        tuple: A dictionary of squares (excluding perfect squares) and the sum of all squares.
    """
    squared_dict = {}
    sum_of_squares = 0

    for i in range(1, n+1):
        square = i ** 2
        if square % i != 0:
            squared_dict[i] = square
            sum_of_squares += square
    
    return squared_dict, sum_of_squares