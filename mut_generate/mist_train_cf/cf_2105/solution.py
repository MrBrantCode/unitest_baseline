"""
QUESTION:
Design a function named `find_max` that takes four numbers as input and returns the maximum number. The function must not use any built-in sorting or comparison functions, loops, recursion, or extra data structures, but can use arithmetic operations, conditional statements, and variable assignments.
"""

def find_max(a, b, c, d):
    max_num = a
    max_num = (b > max_num) * b + (b <= max_num) * max_num
    max_num = (c > max_num) * c + (c <= max_num) * max_num
    max_num = (d > max_num) * d + (d <= max_num) * max_num
    return max_num