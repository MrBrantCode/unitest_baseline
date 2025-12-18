"""
QUESTION:
Implement a recursive function named `factorial` that calculates the factorial of a non-negative integer `n`. The function should have at least three base cases and handle at least three recursive calls within its implementation. The time complexity of the function should be O(2^n), where n is the size of the input.
"""

def factorial(n):
    # Base cases
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    # Recursive calls
    return n * factorial(n-1)