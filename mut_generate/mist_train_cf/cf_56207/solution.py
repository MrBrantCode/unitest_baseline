"""
QUESTION:
Write a function `find_IPs(text)` that uses regular expressions to identify and retrieve every Internet Protocol (IP) address contained within a given text. The function should return a list of IP addresses found in the text, with each address in the format "xxx.xxx.xxx.xxx", where xxx is a number between 0 and 255.
"""

import re

def find_IPs(text):
    pattern = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    return re.findall(pattern, text)