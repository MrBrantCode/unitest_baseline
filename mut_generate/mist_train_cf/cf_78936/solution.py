"""
QUESTION:
Write a function named `multiply` that takes a non-empty list of integers as input and returns the multiplication of those odd elements whose indices are even. The function should use recursion to obtain the end result. The function should assume that the list uses 0-based indexing.
"""

def multiply(lst):
    if len(lst) == 0:
        return 1
    elif lst[0] % 2 != 0:
        return lst[0] * multiply(lst[2:])
    else:
        return multiply(lst[2:]) 