"""
QUESTION:
Create a function called `is_valid_ip_address` that takes a string as input and returns `True` if it is a valid IP address and `False` otherwise, without using any built-in IP address validation functions or regular expressions. The IP address is valid if it consists of exactly 4 parts separated by periods, each part is a number between 0 and 255 (inclusive), and does not have leading zeros (except for '0' itself). The function should have a time complexity of O(1) and a space complexity of O(1).
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