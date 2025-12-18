"""
QUESTION:
Create a function named `is_valid_ipv4` that takes a string as input and returns a boolean indicating whether the string represents a valid IPv4 address. The function should use a regular expression to match the input string. The regular expression should allow for four numbers separated by dots, with each number between 0 and 255 inclusive, and not starting with a zero unless it's zero itself.
"""

import re

def is_valid_ipv4(ip):
    pattern = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    return bool(re.match(pattern, ip))