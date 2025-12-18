"""
QUESTION:
Write a function `factorial(num)` that calculates the factorial of a given non-negative integer `num`. The function should recursively multiply `num` by the factorial of `num - 1` until `num` reaches 0, at which point it should return 1.
"""

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)