"""
QUESTION:
Write a function `multiply(lst)` that calculates the product of all odd elements at even indices within a given non-empty list of integers `lst`.
"""

def multiply(lst):
    product = 1
    for i in range(0, len(lst), 2):
        if lst[i] % 2 != 0:
            product *= lst[i]
    return product