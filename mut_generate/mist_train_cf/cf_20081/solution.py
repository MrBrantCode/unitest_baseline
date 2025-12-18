"""
QUESTION:
Write a function named `factorial(n)` that calculates the factorial of a given non-negative integer `n`. The function should return `None` for negative input and have a time complexity of O(n) and a space complexity of O(1). The function should not use recursion and should handle the base cases where `n` equals 0 or 1.
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