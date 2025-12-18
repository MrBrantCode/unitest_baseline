"""
QUESTION:
Create a function called `replace_ip_address` that takes a string `text` as input, uses regular expressions to find all instances of IP addresses in the text, and replaces them with the term "IP_ADDRESS". The IP addresses to be matched should be in the standard dotted decimal format (e.g., XXX.XXX.XXX.XXX) with each number ranging from 0 to 255.
"""

import re

def replace_ip_address(text):
    ip_regex = r"\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b"
    return re.sub(ip_regex, "IP_ADDRESS", text)