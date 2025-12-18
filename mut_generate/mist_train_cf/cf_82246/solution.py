"""
QUESTION:
Write a function named `sum_of_factorial_digits` that calculates the sum of the digits in the factorial of a given non-negative integer `n`. The function should not take any arguments other than `n`. The factorial is the product of all positive integers up to `n`.
"""

def sum_of_factorial_digits(n):
    """Calculate the sum of digits in the factorial of a number."""
    def factorial(num):
        if num == 0:
            return 1
        else:
            return num * factorial(num - 1)

    def sum_of_digits(num):
        return sum(int(digit) for digit in str(num))

    fact = factorial(n)
    return sum_of_digits(fact)