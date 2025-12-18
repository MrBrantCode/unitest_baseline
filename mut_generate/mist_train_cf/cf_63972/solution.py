"""
QUESTION:
Write a function `aggregate_tuples` that calculates the sum of all numerical values within a list of tuples, including nested tuples and complex numbers, while excluding non-numeric elements.

The function should be able to handle tuples within tuples nested to any level, ignore non-numeric data types, and correctly process floating point numbers and integers. It should also be able to handle edge cases such as empty tuples or tuples with only non-numeric elements, and large inputs without causing performance issues.
"""

def aggregate_tuples(tuples):
    total = 0
    for element in tuples:
        if isinstance(element, tuple):
            total += aggregate_tuples(element)
        elif isinstance(element, (int, float)):
            total += element
        elif isinstance(element, complex):
            total += element.real
    return total