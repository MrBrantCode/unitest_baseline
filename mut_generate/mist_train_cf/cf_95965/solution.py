"""
QUESTION:
Write a function named `factorial(n)` that calculates the factorial of a given integer `n`. The function should use a loop instead of recursion and have a time complexity of O(n) and a space complexity of O(1). The function should return `None` when `n` is negative.
"""

def factorial(n):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n+1):
        result *= i
    
    return result