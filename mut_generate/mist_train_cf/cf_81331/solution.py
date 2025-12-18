"""
QUESTION:
Implement a function `sum_numbers(num1, num2)` that takes two numbers as input, which can be either integers, float values, or strings representing numbers, and returns their sum as a floating point value. If the string inputs are not valid numbers, the function should return `None`.
"""

def sum_numbers(num1, num2):
    try:
        return float(num1) + float(num2)
    except ValueError:
        return None