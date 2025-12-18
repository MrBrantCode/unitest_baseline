"""
QUESTION:
In this Kata we are passing a number (n) into a function. 

Your code will determine if the number passed is even (or not). 

The function needs to return either a true or false. 

Numbers may be positive or negative, integers or floats.

Floats are considered UNeven for this kata.
"""

def is_even_or_odd(n):
    # Check if the number is an integer
    if isinstance(n, int):
        return n % 2 == 0
    # If the number is a float, return False
    return False