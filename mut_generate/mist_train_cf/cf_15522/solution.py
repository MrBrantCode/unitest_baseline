"""
QUESTION:
Create two functions, `factorial(n)` and `sum_of_factorials(n)`, where `n` is a non-negative integer. The `factorial(n)` function should calculate the factorial of `n`, and the `sum_of_factorials(n)` function should calculate the sum of all factorials from 1 to `n`. The functions should not take any additional parameters besides `n`.
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def sum_of_factorials(n):
    sum = 0
    for i in range(1, n+1):
        sum += factorial(i)
    return sum