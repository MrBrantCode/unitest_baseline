"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given integer `n`. The function should use a loop instead of recursion and have a time complexity of O(n) and a space complexity of O(1). It should also handle negative integers and return the corresponding result. The function can only use a single variable to store intermediate values and cannot use any built-in mathematical functions or operators.
"""

def factorial(n):
    if n < 0:
        return "Invalid input"
    elif n == 0:
        return 1

    result = 1
    for i in range(1, abs(n) + 1):
        result *= i

    if n < 0 and n % 2 == 1:
        return -result
    else:
        return result