"""
QUESTION:
Implement a function `squares_roots_dictionary` that takes a list of numbers as input, calculates their squares and square roots, and returns them in a dictionary. The function should use dictionary comprehensions, ignore any numbers that are already present in the dictionary, and handle non-numeric values by ignoring them. The input numbers can be either integers or floats.
"""

def squares_roots_dictionary(numbers):
    return {num: (num*num, num**0.5) for num in set(numbers) if isinstance(num, (int, float))}