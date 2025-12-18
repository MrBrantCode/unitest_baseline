"""
QUESTION:
Write a function named `factorial` to calculate the factorial of a non-negative integer `n` iteratively without using the built-in `math.factorial()` function, with a time complexity of O(n) and constant space complexity.
"""

def factorial(n):
    if n == 0:
        return 1
    
    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result