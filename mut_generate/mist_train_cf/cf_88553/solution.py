"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a non-negative integer `n` using at least three base cases and handles at least three recursive calls. The function should have a time complexity of O(2^n).
"""

def entance(n):
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Recursive calls
    return n * entance(n-1)