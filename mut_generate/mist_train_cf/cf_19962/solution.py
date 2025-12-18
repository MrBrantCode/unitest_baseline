"""
QUESTION:
Write a function `calculate_factorial(num)` that calculates the factorial of a given number. The function should return the product of all positive integers less than or equal to `num`. If `num` is negative, return an error message indicating that the factorial is not defined for negative numbers.
"""

def calculate_factorial(num):
    if num < 0:
        return "Error: Factorial is not defined for negative numbers."
    elif num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, num+1):
            factorial *= i
        return factorial