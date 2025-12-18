"""
QUESTION:
Write a function `calculate_factorial(n)` that calculates the factorial of a given number `n` using an iterative approach to handle large inputs. The function should take an integer `n` as input and return the factorial of `n`. The function should be able to handle inputs up to 1000.
"""

def calculate_factorial(n):
    factorial = 1

    for i in range(1, n+1):
        factorial *= i

    return factorial