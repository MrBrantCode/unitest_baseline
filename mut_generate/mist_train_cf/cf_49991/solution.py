"""
QUESTION:
Write a function `factorial(number)` that calculates the factorial product of a given integer `number`. The function should return the product of all integers from 1 to `number`. Implement the function using either a recursive or iterative approach.
"""

def factorial(number):
    factorial_product = 1
    for i in range(1, number + 1):
        factorial_product *= i
    return factorial_product