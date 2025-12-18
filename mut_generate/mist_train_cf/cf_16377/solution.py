"""
QUESTION:
Write a function called `calculate_factorial` that takes a single integer `n` as input and returns the product of all positive odd integers less than or equal to `n`. The function should handle negative inputs by returning an error message. If `n` is 0 or 1, the function should return 1.
"""

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(n, 0, -2):
            if i % 2 != 0:
                factorial *= i
        return factorial