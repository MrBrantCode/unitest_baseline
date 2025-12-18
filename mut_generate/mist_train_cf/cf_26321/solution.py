"""
QUESTION:
Write a function `isValidIP(ip)` to check if the input string `ip` is a valid IP address. A valid IP address consists of four numbers separated by dots, and each number is between 0 and 255 inclusive. The function should return `True` if the string is a valid IP address and `False` otherwise.
"""

import re

def isValidIP(ip): 
    regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
            25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
    pattern = re.compile(regex) 
    return bool(pattern.search(ip))