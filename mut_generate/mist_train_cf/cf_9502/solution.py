"""
QUESTION:
Write a function `is_valid_ipv4(ip_address)` that determines whether the given string is a valid IPv4 address. The function should return `True` if the string is a valid IPv4 address and `False` otherwise. A valid IPv4 address consists of four octets separated by dots, each octet is a number between 0 and 255 (inclusive), and leading zeros are not allowed.
"""

def is_valid_ipv4(ip_address):
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False
    
    for octet in octets:
        if not octet.isdigit():
            return False
        if not 0 <= int(octet) <= 255:
            return False
        if octet != str(int(octet)):
            return False
    
    return True