"""
QUESTION:
Write a function named `factorial` to calculate the factorial of a given number `n` using a while loop. The function should return the factorial of `n`. Note that the factorial of 0 and 1 is 1.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result