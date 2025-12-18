"""
QUESTION:
Implement a function named `factorial` that takes an integer `n` as input and returns the factorial of `n`. The function should return `None` for negative numbers and `1` for `n = 0`. The time complexity should be O(n).
"""

def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result