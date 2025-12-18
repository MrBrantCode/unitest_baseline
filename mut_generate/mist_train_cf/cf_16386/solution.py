"""
QUESTION:
Write a recursive function named `factorial(n)` that takes a positive integer `n` as input and returns two values: the factorial of `n` and the number of digits in the factorial. The function should work for `n = 0` and `n = 1`, where the factorial is 1 and the number of digits is 1.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1, 1
    else:
        factorial_num, num_of_digits = factorial(n - 1)
        factorial_num *= n
        num_of_digits = len(str(factorial_num * n))
        return factorial_num, num_of_digits