"""
QUESTION:
Write a function `add_100` that takes a sentence as input and returns the sentence with all numbers that are divisible by 3 or 4 increased by 100. The function should use regular expressions to find the numbers in the sentence.
"""

import re

def add_100(sentence):
    pattern = r'\d+'
    def replace(match):
        num = int(match.group())
        if num % 3 == 0 or num % 4 == 0:
            return str(num + 100)
        else:
            return str(num)
    return re.sub(pattern, replace, sentence)