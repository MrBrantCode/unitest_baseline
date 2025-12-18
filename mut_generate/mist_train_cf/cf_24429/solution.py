"""
QUESTION:
Construct a function `is_valid_ip` that determines whether a given string represents a valid IP address. The function should return a boolean value indicating whether the string is a valid IP address. The IP address is considered valid if it consists of four numbers separated by dots, each number is between 0 and 255, and the number does not have leading zeros unless it's 0 itself.
"""

def is_valid_ip(ip):
    parts = ip.split(".")
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        if len(part) > 1 and part[0] == '0':
            return False
        if int(part) < 0 or int(part) > 255:
            return False
    
    return True