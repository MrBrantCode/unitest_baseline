"""
QUESTION:
Write a function `extract_key_value_pairs(inpStr: str) -> dict` that takes a string `inpStr` containing key-value pairs in the format "[key]=[value]" and returns a dictionary with the extracted key-value pairs. The input string may contain multiple key-value pairs separated by commas, and keys and values are enclosed in square brackets. The function should handle cases where the input string is empty or contains invalid key-value pair formats.
"""

import re

def extract_key_value_pairs(inpStr: str) -> dict:
    key_value_pairs = re.findall(r'\[(.+?)]=\[(.+?)]', inpStr)
    return dict(key_value_pairs)