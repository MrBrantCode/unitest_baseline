"""
QUESTION:
Create a function `is_even_or_odd` that takes a non-negative integer `num` as input and returns a string indicating whether the number is even or odd. The function should return "Even" for even numbers and "Odd" for odd numbers. The function should have a time complexity of O(1) and cannot use built-in functions or libraries to determine whether a number is even or odd.
"""

def is_even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"