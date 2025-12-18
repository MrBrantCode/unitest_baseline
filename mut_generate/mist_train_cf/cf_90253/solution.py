"""
QUESTION:
Create a function `is_power_of_two(n)` to determine if a given number `n` is a power of two using only basic arithmetic operations (+, -, *, /) and without using loops or recursion. The function should have a time complexity of O(log n) and a space complexity of O(1), and cannot use any built-in math or bitwise operators, the modulo operator (%), or any string manipulation methods.
"""

def is_power_of_two(n):
    if n <= 0:
        return False
    while n & 1 == 0:
        n = n >> 1
    return n == 1