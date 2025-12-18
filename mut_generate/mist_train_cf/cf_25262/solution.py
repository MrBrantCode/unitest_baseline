"""
QUESTION:
Write a function `extract_phone_numbers(text)` that takes a string of text as input and returns all the phone numbers present in the text. The phone numbers are in the format (XXX) XXX-XXXX, where X is a digit. The function should return the phone numbers as a list of strings.
"""

import re

def extract_phone_numbers(text): 
    phones = re.findall("\(\d{3}\) \d{3}\-\d{4}",text) 
    return phones