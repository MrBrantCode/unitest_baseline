"""
QUESTION:
Write a function named `test_input` that takes a string as input and returns `True` if the string represents a three-digit prime number and `False` otherwise. The function should first check if the input string consists of exactly three digits using a regular expression, and then verify if the corresponding integer is a prime number.
"""

import re

def test_input(user_input):
    regex = '^\\d{3}$'
    pattern = re.compile(regex)
    match = pattern.match(user_input)
    if match:
        num = int(user_input)
        if num == 1:
            return False
        elif num == 2:
            return True
        else:
            for x in range(2, num):
                if num % x == 0:
                    return False
            return True 
    return False