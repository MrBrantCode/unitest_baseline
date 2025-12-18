"""
QUESTION:
Write a function `is_valid_ipv4_address(ip_address)` that takes a string `ip_address` as input and returns `True` if it is a valid IPv4 address and `False` otherwise. A valid IPv4 address consists of four decimal numbers, separated by periods, where each decimal number is between 0 and 255, and leading zeros are not allowed. The function should handle edge cases such as empty strings, non-digit characters, more or less than four decimal numbers, decimal numbers greater than 255, and leading or trailing whitespace. The function should also return `False` if the IP address starts with "0", ends with ".0", or contains consecutive periods. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def is_valid_ipv4_address(ip_address):
    if len(ip_address) == 0:
        return False
    
    parts = ip_address.split('.')
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit() or part.startswith('0') and len(part) > 1 or int(part) > 255:
            return False
    
    if any(part == '' for part in parts):
        return False
    
    if ip_address.startswith('0') and len(ip_address) > 1 or ip_address.endswith('.0'):
        return False
    
    if '..' in ip_address:
        return False
    
    return True