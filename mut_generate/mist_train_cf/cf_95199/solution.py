"""
QUESTION:
Create a function named `factorial` that calculates the factorial of a given non-negative integer `n` without using any built-in functions or libraries. The function should return the calculated factorial and should be able to handle the case where `n` is 0, in which case it should return 1.
"""

def factorial(n):
    result = 1
    
    # Iteratively multiply the result by numbers from 1 to n
    for i in range(1, n+1):
        result *= i
    
    return result