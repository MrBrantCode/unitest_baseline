"""
QUESTION:
Create a function called `extract_numbers` that takes a string of text as input and returns a list of integers. The function should extract all numerical entities (sequences of one or more digits) from the input text and convert them to integers.
"""

import re

def extract_numbers(text):
    numbers = re.findall(r'\d+', text)
    return [int(num) for num in numbers]