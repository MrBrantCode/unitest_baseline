"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given integer `n` without using any built-in functions or libraries. The function should handle non-negative integers, including 0, and return the calculated factorial. The factorial of 0 is defined as 1.
"""

def factorial(n):
    result = 1
    
    # Iteratively multiply the result by numbers from 1 to n
    for i in range(1, n+1):
        result *= i
    
    return result