"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given positive integer `n`, where `n` is less than or equal to 10. If `n` does not meet these conditions, the function should return an error message.
"""

def factorial(n):
    if n < 0 or n > 10:
        return "Invalid input! Please enter a positive number less than or equal to 10."
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n+1):
            fact *= i
        return fact