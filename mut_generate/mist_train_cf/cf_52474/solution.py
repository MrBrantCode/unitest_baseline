"""
QUESTION:
Create a function `is_complex(num)` that takes a string `num` as input and returns `True` if it represents a valid complex number in the format 'a+bi' or 'a-bi', where 'a' and 'b' are integers or decimals, and 'i' represents the imaginary unit. The function should be able to handle optional '+' or '-' characters at the start of the string, as well as optional decimal points in 'a' and 'b'.
"""

import re

def is_complex(num):
    pattern = r"^[-+]?\d*\.?\d+[+-]\d*\.?\d*i$"
    return bool(re.match(pattern, num))