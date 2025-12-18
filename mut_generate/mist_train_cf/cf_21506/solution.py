"""
QUESTION:
Create a Python function `calculate_factorial_sum` that takes two positive integers `num1` and `num2` as input, checks if they are within the range of 1 to 10, and returns the sum of their factorials if valid. If either number is not within the range, return the string "Input numbers should be within the range of 1 to 10."
"""

def calculate_factorial_sum(num1, num2):
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    if num1 < 1 or num1 > 10 or num2 < 1 or num2 > 10:
        return "Input numbers should be within the range of 1 to 10."
    else:
        factorial_sum = factorial(num1) + factorial(num2)
        return factorial_sum