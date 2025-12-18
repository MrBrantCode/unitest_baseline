"""
QUESTION:
Construct a function named `recursive_multiply` that takes a list and an integer `n` as required arguments, and an optional initial product value, to recursively multiply each element of the list with the overall product. The function should return the current product when the list is exhausted or the product exceeds `n`.
"""

def recursive_multiply(lst, n, prod=1):
    if not lst or prod > n:
        return prod
    else:
        return recursive_multiply(lst[1:], n, prod*lst[0])