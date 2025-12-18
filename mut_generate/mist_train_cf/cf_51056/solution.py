"""
QUESTION:
Create a function named `multiply_abs_values` that takes a list of numbers as input, calculates the product of the integer part of their absolute values (excluding any numbers with absolute values greater than 100), and returns the result. The function should handle both integers and floating-point numbers in the input list.
"""

def multiply_abs_values(lst):
    """
    For a given list of numeric entities, compute the product of each element's absolute value, truncating any fractional part to zero if present. Omit from calculations those figures exceeding 100.
    """
    product = 1
    for num in lst:
        if abs(num) <= 100:
            product *= int(abs(num))
    return product