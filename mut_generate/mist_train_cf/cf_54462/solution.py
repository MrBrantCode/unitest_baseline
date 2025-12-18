"""
QUESTION:
Write a function `extract_phonenumbers` that takes a list of text strings and returns a list of phone numbers found. Phone numbers can be in various formats, such as xxx-xxx-xxxx, (xxx)xxx-xxxx, xxx.xxx.xxxx, etc. The function should use regular expressions to identify and extract phone numbers with exactly 10 digits.
"""

import re

def extract_phonenumbers(text_list):
    phone_numbers = []
    phone_regex = re.compile(r'\(?\b\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b')
    for text in text_list:
        matches = phone_regex.findall(text)
        phone_numbers.extend(matches)
    return phone_numbers