"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given integer `n` using a recursive algorithm in a single line of code. The function should have a time complexity of O(n) and space complexity of O(n).
"""

def entance(n):
    return 1 if n == 0 else n * entance(n-1)