"""
QUESTION:
Implement a function named `factorial` that calculates the factorial of a given positive integer `n`. The function should return the product of all positive integers less than or equal to `n`. The function should only accept positive integer inputs and return 1 for `n = 0`. If the input is not a positive integer, the function should return "Invalid input".
"""

def factorial(n):
    if n == 0:
        return 1
    elif n < 0 or not isinstance(n, int):
        return "Invalid input"
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result