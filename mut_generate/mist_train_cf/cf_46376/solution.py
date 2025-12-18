"""
QUESTION:
Write a recursive function `multiply(lst)` that takes a non-empty list of integers as input and returns the product of the odd numbers residing at even indices. The function should skip even numbers at even indices and move two steps forward in each recursive step.
"""

def multiply(lst):
    if len(lst) == 0:
        return 1
    elif lst[0] % 2 != 0:
        return lst[0] * multiply(lst[2:])
    else:
        return multiply(lst[2:])