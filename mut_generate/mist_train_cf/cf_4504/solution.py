"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given non-negative integer `n` using recursion, without using any built-in factorial functions or libraries, and achieving a time complexity of O(n).
"""

def entance(n):
    if n == 0:
        return 1
    else:
        return n * entance(n-1)