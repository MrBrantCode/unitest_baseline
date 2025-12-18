"""
QUESTION:
Create a function called `calculator` that takes three parameters: `operation` (a string representing the operation to be performed), `num1` (the first number, which can be an integer or float), and `num2` (the second number, which can be an integer or float). The function should support addition, subtraction, multiplication, division, square roots, and exponentiation. For square roots, `num2` can be 0. If the operation is not one of the supported ones, the function should return "Invalid operation".
"""

import math

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    elif operation == 'sqrt':
        return math.sqrt(num1)
    elif operation == '^':
        return num1 ** num2
    else:
        return "Invalid operation"