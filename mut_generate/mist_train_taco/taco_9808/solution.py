"""
QUESTION:
Find a*b, for all given number pairs

SAMPLE INPUT
5
4 6
3 7

SAMPLE OUTPUT
24
21
"""

def multiply_pairs(pairs):
    """
    Multiplies each pair of numbers in the input list and returns a list of the products.

    Parameters:
    pairs (list of tuples): A list where each tuple contains two integers.

    Returns:
    list of int: A list of integers where each integer is the product of the corresponding pair of numbers.
    """
    return [a * b for a, b in pairs]