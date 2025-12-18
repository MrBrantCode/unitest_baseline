"""
QUESTION:
Write a function called `generate_even_squares` that generates a list of squares of all even numbers within a given range, from 1 to n (inclusive), where n is a positive integer. The function should use list comprehension.
"""

def generate_even_squares(n):
    return [x**2 for x in range(1, n+1) if x % 2 == 0]