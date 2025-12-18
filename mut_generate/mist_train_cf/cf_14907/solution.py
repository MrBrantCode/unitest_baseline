"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given number `n`. The input `n` should be a positive integer (>= 1). If `n` is not a positive integer, the function should return an error message. If `n` is negative, the function should calculate the factorial of its absolute value. Do not use built-in functions or libraries for calculating the factorial.
"""

def calculate_factorial(n):
    if type(n) != int or n < 1:
        return "Input must be a positive integer"
    else:
        result = 1
        for i in range(1, abs(n)+1):
            result *= i
        return result