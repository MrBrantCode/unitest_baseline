"""
QUESTION:
Create a function `sumToN` that takes an integer `n` as input and returns the sum of the squares of all integers from 1 to `n` using a mathematical formula. The time complexity of the function should be O(1), meaning it should not use iteration or recursion that scales with the input size.
"""

def sumToN(n):
    return n * (n + 1) * (2 * n + 1) // 6