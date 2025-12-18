"""
QUESTION:
Write a function `extract_licenses(text: str) -> List[str]` that takes a string `text` as input and returns a list of all the license names found in the text. The license information is enclosed within a specific format, where the license name is the text between "Licensed under the " and " (the "License");". The function should return all occurrences of the license names found in the text.
"""

from typing import List
import re

def extract_licenses(text: str) -> List[str]:
    pattern = r'Licensed under the (.+?) \(the "License"\);'
    licenses = re.findall(pattern, text, re.DOTALL)
    return licenses