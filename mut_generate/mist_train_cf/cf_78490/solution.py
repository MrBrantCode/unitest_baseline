"""
QUESTION:
Create a function called `frequency` that generates a dictionary containing elements from list `x` as keys and their occurrence frequency in both list `x` and list `y` as values. The function should take two parameters: `x` and `y`, both of which are lists of integers. Return the resulting dictionary.
"""

from collections import Counter

def frequency(x, y):
    """Generates a dictionary containing elements from list `x` as keys 
    and their occurrence frequency in both list `x` and list `y` as values."""
    return Counter(x + y)