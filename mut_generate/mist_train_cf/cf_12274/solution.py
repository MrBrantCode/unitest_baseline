"""
QUESTION:
Develop a function to validate if a given string is a valid IP address. The function should return True if the string is a valid IP address, and False otherwise. The function name should be `is_valid_ip`.
"""

def is_valid_ip(ip_address):
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    for item in parts:
        if not item.isdigit():
            return False
        if not 0 <= int(item) <= 255:
            return False
        if len(item) > 1 and item[0] == '0':
            return False
    return True