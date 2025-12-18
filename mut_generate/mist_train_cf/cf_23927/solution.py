"""
QUESTION:
Implement a function `isvalid_ip(string)` to check if a given string is a valid IP address. A valid IP address consists of four numbers between 0 and 255 separated by dots, with each number not exceeding three digits. The function should return True if the string is a valid IP address, and False otherwise.
"""

import re

def isvalid_ip(string):
    regex = r"^(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)(?:\.(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)){3}$"
    return bool(re.search(regex, string))