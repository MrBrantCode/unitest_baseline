"""
QUESTION:
Write a function named `multiply(lst)` that takes a non-empty list of integers `lst` and returns the product of all odd elements located at even indices. The function should only consider indices that are even (0-based indexing).
"""

def multiply(lst):
    product = 1
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            product *= lst[i]
    return product