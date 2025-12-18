"""
QUESTION:
Write a function `sum_of_pairs` that takes a list of tuples as input, where each tuple contains three integers. The function should return a new list containing the sum of the first two elements of each tuple.
"""

def sum_of_pairs(pairs):
    return [a + b for a, b, c in pairs]