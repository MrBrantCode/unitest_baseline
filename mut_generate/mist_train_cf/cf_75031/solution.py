"""
QUESTION:
Write a function `max_num` in Python that finds the maximum number in a list of integers without using the built-in `max` function or any sorting functions. The function should be able to handle lists containing both positive and negative integers, as well as zero.
"""

def max_num(lst):
    max_val = lst[0]
    for num in lst:
        if num > max_val:
            max_val = num
    return max_val