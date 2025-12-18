"""
QUESTION:
Write a function called `add_100` that takes a string of text as input, finds all sequences of digits in the text using regular expressions, adds 100 to the numbers that are divisible by 3 or 4, and returns the modified text. The function should return the original numbers unchanged if they are not divisible by 3 or 4.
"""

import re

def add_100(match):
    num = int(match.group())
    if num % 3 == 0 or num % 4 == 0:
        return str(num + 100)
    else:
        return str(num)