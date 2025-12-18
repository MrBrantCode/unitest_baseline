"""
QUESTION:
Implement a function named `factorial(n)` that calculates the factorial of a given non-negative integer `n` using iteration. The function should have a time complexity of O(n) and a constant space complexity.
"""

def factorial(n):
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result