"""
QUESTION:
Create a function `do_calculations` that takes two parameters: `operators` and `operands`. The function should perform mathematical operations on the `operands` based on the `operators` and return the result. The `operators` list can contain the following operations: +, -, *, //, **, log, exp, sin, cos, tan. The `operands` list contains non-negative integers and angles in degrees. The length of the `operators` list is equal to the length of the `operands` list minus one. The function should use the math module for logarithmic, exponential, and trigonometric calculations and handle the operations sequentially. The result should be rounded to three decimal places.
"""

import math
from functools import reduce

operators_dict = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "//": lambda x, y: x // y,
    "**": lambda x, y: x ** y,
    "log": lambda x, y: math.log(x, y),
    "exp": lambda x, y: x * math.exp(y),
    "sin": lambda x, y: x * math.sin(math.radians(y)),
    "cos": lambda x, y: x * math.cos(math.radians(y)),
    "tan": lambda x, y: x * math.tan(math.radians(y)),
}

def do_calculations(operators, operands):
    return round(reduce(lambda a, b: operators_dict[operators[operands.index(b) - 1]](a, b), operands), 3)