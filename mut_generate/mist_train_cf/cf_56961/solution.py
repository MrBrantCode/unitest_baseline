"""
QUESTION:
Write a function `factorial(n)` to calculate the factorial of a number `n`. The function should not use any built-in functions or libraries for factorial calculation and should be able to handle large values of `n` without causing a stack overflow error. Also, analyze the time and space complexity of the solution.
"""

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result