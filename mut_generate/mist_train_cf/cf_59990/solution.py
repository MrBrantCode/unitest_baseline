"""
QUESTION:
Develop a function named `product_of_integers` that calculates the product of all integers in a given list. The function should ignore non-integer or missing data and continue the calculation only with the integer values. The input list can be of any length and may contain integers, non-integer values, and None.
"""

def product_of_integers(data):
    # Base Case
    if not data:
        return 1

    # Recursive Case
    first, *rest = data
    if isinstance(first, int):
        return first * product_of_integers(rest)
    
    # Non-integer or missing data, continue with the rest of the list
    else:
        return product_of_integers(rest)