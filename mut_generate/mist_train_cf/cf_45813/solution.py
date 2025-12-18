"""
QUESTION:
Design a function `extract_data(html_string)` that uses regular expressions to extract substrings found within HTML tags from a given string `html_string`, considering any HTML tag. The function should return a list of extracted substrings.
"""

import re

def extract_data(html_string):
    pattern = '<.*?>(.*?)</.*?>'
    result = re.findall(pattern, html_string)
    return result