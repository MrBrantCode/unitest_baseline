"""
QUESTION:
Create a function named `harmonic_integration` that takes a list of integers as input and returns their harmonic sum, calculated as the sum of the reciprocals of the input numbers. The input list is not empty and contains only positive integers.
"""

def harmonic_integration(numbers):
    """Calculate the harmonic sum of a list of integers."""
    return sum(1 / number for number in numbers)