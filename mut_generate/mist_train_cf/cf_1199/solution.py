"""
QUESTION:
Write a function named `sub` that takes two integers `a` and `b` as input and returns the result of `a` minus `b` without using the subtraction operator (-). The function should have a time complexity better than O(|b|).
"""

def sub(a, b):
    return a + (~b + 1)