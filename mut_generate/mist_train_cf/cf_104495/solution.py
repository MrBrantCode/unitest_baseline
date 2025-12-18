"""
QUESTION:
Implement a function `multiply_and_replace(lst, size)` that takes a list of integers `lst` and a positive integer `size` as input. The function should return a new list where each element of `lst` is multiplied by three, and any resulting value greater than `size` is replaced with `size`. If `lst` is empty, the function should return an empty list.
"""

def multiply_and_replace(lst, size):
    return [min(num * 3, size) for num in lst]