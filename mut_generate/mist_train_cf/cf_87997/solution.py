"""
QUESTION:
Write a function `is_valid_ipv4_address(ip_address)` that takes in a string and returns `True` if it is a valid IPv4 address and `False` otherwise. A valid IPv4 address consists of four decimal numbers, separated by periods, where each decimal number is between 0 and 255. Leading zeros are not allowed. The function should handle edge cases such as empty strings, non-numeric characters, more or less than four decimal numbers, decimal numbers greater than 255, and leading or trailing whitespace. The time complexity of the solution should be O(n), where n is the length of the input string.
"""

def is_valid_ipv4_address(ip_address):
    if len(ip_address) == 0:
        return False
    
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit() or (len(part) > 1 and part.startswith('0')) or int(part) > 255:
            return False
    
    return True