"""
QUESTION:
Create a function `add_100` that takes a string containing numbers and adds 100 to the numbers that are divisible by 3 or 4, leaving other numbers unchanged. Use regular expressions in Python to find and replace the numbers in the string.
"""

import re

def add_100(match):
    num = int(match.group())
    if num % 3 == 0 or num % 4 == 0:
        return str(num + 100)
    else:
        return str(num)