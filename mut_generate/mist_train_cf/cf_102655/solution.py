"""
QUESTION:
Write a function named factorial(n) that calculates the factorial of a given non-negative integer n using a loop structure. The function should return None and display an error message if n is negative.
"""

def factorial(n):
    if n < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None

    result = 1
    for i in range(1, n+1):
        result *= i
    
    return result