"""
QUESTION:
Write a function `calculate_numeric_sum(markup)` that takes a string `markup` as input and returns the sum of all numeric values found in the attributes of the given markup language. The function should extract attribute-value pairs from the markup string, identify numeric values, and calculate their sum.
"""

import re

def calculate_numeric_sum(markup):
    pattern = r'(\w+)\s*=\s*"?(\d+\.?\d*|[+-]?\d*\.\d+)"?'
    matches = re.findall(pattern, markup)
    numeric_sum = 0
    for attr, value in matches:
        try:
            numeric_sum += float(value)
        except ValueError:
            continue
    return numeric_sum