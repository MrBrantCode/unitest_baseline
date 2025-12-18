"""
QUESTION:
Write a function `factorial(n)` that computes the factorial of a given positive integer `n` using recursion. The input number `n` should be less than or equal to 10. The function should not use any loops or global variables. If `n` is greater than 10, the function should return an error message.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 10:
        return "Input number should be less than or equal to 10."
    else:
        return n * factorial(n-1)