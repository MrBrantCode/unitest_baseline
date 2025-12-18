"""
QUESTION:
Create a function `is_power_of_two` to determine whether a given number is a power of two. The function should have a time complexity of O(1) and a space complexity of O(1), and only use basic arithmetic operations (+, -, *, /). You cannot use loops, recursion, string manipulation, or modulo operator.
"""

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0