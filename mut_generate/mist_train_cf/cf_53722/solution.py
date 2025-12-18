"""
QUESTION:
Create a function `isValidIP` that determines if a given string contains a valid IPv4 address. The function should return `True` if a valid IP address is found and `False` otherwise. The input string may contain other characters and the IP address may be part of a URL. The function should only consider IPv4 addresses in the format of four numbers separated by dots, with each number ranging from 0 to 255.
"""

import re

def isValidIP(string):
    # Define regular expression for IPv4
    regex = r"\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3})\b"
 
    # Create pattern object
    p = re.compile(regex)

    # Return True if valid IP found else False
    return bool(re.search(p, string))