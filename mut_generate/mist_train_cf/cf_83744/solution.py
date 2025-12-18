"""
QUESTION:
Create a function `extract_ipv4_addresses(text)` that recognizes and extracts all IPv4 addresses from a given block of text. The function should return a list of strings, where each string is a valid IPv4 address in the input text. An IPv4 address consists of four parts separated by dots, with each part being a number from 0 to 255.
"""

import re

def extract_ipv4_addresses(text):
    ipv4_pattern = r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b'
    return re.findall(ipv4_pattern, text)