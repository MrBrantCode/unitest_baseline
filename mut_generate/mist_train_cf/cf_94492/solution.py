"""
QUESTION:
Write a function `is_valid_ip_address(ip_address)` that checks if a given string `ip_address` is a valid IP address without using built-in IP address validation functions or regular expressions. The function should return `True` if the IP address is valid and `False` otherwise, with a time complexity of O(1) and a space complexity of O(1). The IP address should consist of four parts separated by periods ('.') with each part being a number between 0 and 255 (inclusive) and not having leading zeros (except for '0' itself).
"""

def is_valid_ip_address(ip_address):
    parts = ip_address.split('.')

    if len(parts) != 4:
        return False

    for part in parts:
        if not part or (part[0] == '0' and len(part) > 1):
            return False

        try:
            value = int(part)
        except ValueError:
            return False

        if value < 0 or value > 255:
            return False

    return True