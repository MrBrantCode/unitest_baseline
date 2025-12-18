"""
QUESTION:
Write a function `validate_ip_address` that takes a string as input and returns a boolean indicating whether it is a valid IP address. A valid IP address consists of four numbers separated by dots, and each number must be between 0 and 255, inclusive. The function should return True if the input string is a valid IP address and False otherwise.
"""

import re

def validate_ip_address(ip):
    pattern = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    return bool(re.match(pattern, ip))