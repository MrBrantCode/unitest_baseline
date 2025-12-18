"""
QUESTION:
Write a function called "swap_values" that takes two variables as arguments and returns their swapped values without using any built-in functions or temporary variables. The function should update the values in-place and be efficient in terms of space and time complexity.
"""

def swap_values(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b