"""
QUESTION:
Create a function called `factorial(n)` that calculates the factorial of a given integer `n`. The function should only accept non-negative integers as input and return an error message for negative integers. The function should return 1 for inputs 0 and 1, and the product of all positive integers less than or equal to `n` for other non-negative integers.
"""

def factorial(n):
    # Check if input n is a non-negative integer
    if not isinstance(n, int) or n < 0:
        return "Error: Factorial is undefined for negative integers."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact