"""
QUESTION:
Implement a function `multiply_and_replace` that takes a list of integers `lst` and a positive integer `size` as input. The function should return a new list where each element in `lst` is multiplied by 3, but capped at `size` if the product exceeds it. If `lst` is empty, an empty list should be returned.
"""

def multiply_and_replace(lst, size):
    return [min(num * 3, size) for num in lst]