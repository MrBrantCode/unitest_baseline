"""
QUESTION:
Create a Calculator class with methods for add, subtract, multiply, divide, square_root, and power. The methods should accept only positive numbers as input and handle potential errors or exceptions. 

The add, subtract, multiply, and divide methods should take two numbers as input and return the corresponding result. The divide method should raise a ValueError if the second number is zero.

The square_root method should take one number as input, raise a ValueError if the number is negative, and return the square root of the number.

The power method should take two numbers as input, raise a ValueError if the base number is negative and the exponent is not an integer, and return the result of raising the base number to the exponent.
"""

import math

def calculator(num1, num2, operation):
    operations = {
        'add': num1 + num2,
        'subtract': num1 - num2,
        'multiply': num1 * num2,
        'divide': num1 / num2 if num2 != 0 else float('inf'),
        'square_root': math.sqrt(num1) if num1 >= 0 else float('nan'),
        'power': num1 ** num2 if num1 >= 0 or num2 == int(num2) else float('nan')
    }

    return operations.get(operation, 'Invalid operation')