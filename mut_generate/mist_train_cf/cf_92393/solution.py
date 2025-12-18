"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given non-negative integer `n` using a loop instead of recursion. The function should return `None` for negative input values and have a time complexity of O(n) and a space complexity of O(1).
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