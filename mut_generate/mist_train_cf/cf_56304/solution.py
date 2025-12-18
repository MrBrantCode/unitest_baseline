"""
QUESTION:
Write a recursive function named `invert` that takes a nested list of integers as input. The function should reverse the order of the elements at each level of nesting, and also reverse the order of the sublists themselves. For example, given the input `[1, [2,3,4, [5,6]], 7]`, the output should be `[7, [[6,5], 4, 3, 2], 1]`.
"""

def invert(lst):
    return [invert(i) if isinstance(i, list) else i for i in lst[::-1]]