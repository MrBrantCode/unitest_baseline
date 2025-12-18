"""
QUESTION:
Write a function `product_list` that calculates the product of a list of numbers, where the list can contain both integers and real numbers. The function should handle edge cases such as an empty list, single-number lists, or lists with zero. The function should return a float value and should not use any external libraries.
"""

def product_list(items):
    total = 1.0 
    for num in items:
        total *= num
    return total