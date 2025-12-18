"""
QUESTION:
Create a function `compare_num(a, b)` that compares two numbers `a` and `b` and returns -1 if `a` is less than `b`, 0 if `a` equals `b`, and 1 if `a` is greater than `b`. The function must use the ternary operator, have a time complexity of O(1), and be implemented in a single line without using any if-else statements.
"""

def compare_num(a, b):
    return -1 if a < b else (0 if a == b else 1)