"""
QUESTION:
Create a function `is_numerical` that takes a string as input and returns a boolean indicating whether the string represents a numerical value, including signed integers, floating point numbers, and scientific notation. The function should correctly identify negative values and zero (with or without a decimal point).
"""

import re

def is_numerical(input_string):
    numerical_re = re.compile(r'^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$')
    return bool(numerical_re.match(input_string))