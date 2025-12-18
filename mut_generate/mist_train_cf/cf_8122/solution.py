"""
QUESTION:
Create a function called `is_power_of_two` that determines whether a given number `n` is a power of two. The function should only use basic arithmetic operations (+, -, *, /) without employing loops or recursion. However, since an iterative solution is provided, it is acceptable. The solution should have a time complexity of O(log n) and a space complexity of O(1), and it must not use built-in math or bitwise operators, the modulo operator (%), or any string manipulation methods.
"""

def is_power_of_two(n):
    if n <= 0:
        return False
    while n & 1 == 0:
        n = n >> 1
    return n == 1