"""
QUESTION:
Design a function named `find_ip` that takes a string as an input and returns a list of valid IP addresses found in the string. A valid IP address consists of four numbers between 0 and 255 separated by dots. The function should use regular expressions to extract possible IP address patterns and then validate each extracted pattern to ensure that each number is within the valid range.
"""

import re

def find_ip(string):
    pattern = r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b"
    ip = re.findall(pattern, string)

    valid_ip = []
    for i in ip:
        if all(map(lambda x: 0<=int(x)<=255, i.split('.'))):
            valid_ip.append(i)
    
    return valid_ip