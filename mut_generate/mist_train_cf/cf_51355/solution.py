"""
QUESTION:
Construct a function `deep_sum` that takes a nested list of numbers as an argument and returns the sum of all numbers in the list, using only iterative logic and without any built-in Python flatten mechanism. The function should be able to handle lists containing other lists of any depth.
"""

def deep_sum(lst):
    total = 0
    stack = lst[:]
    while stack:
        item = stack.pop(0)
        if type(item) is list:
            stack = item + stack
        else:
            total += item
    return total