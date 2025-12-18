"""
QUESTION:
Write a function `is_valid_ipv6(address)` that checks whether a given string `address` is a valid IPv6 address. A valid IPv6 address consists of 8 groups of hexadecimal digits separated by colons. Each group should be a valid hexadecimal number between 0 and 65535 (inclusive). Leading zeros in each group are allowed, but not required. The function should return `True` if the address is valid and `False` otherwise.
"""

def is_valid_ipv6(address):
    # Split the address into 8 groups separated by colons
    groups = address.split(':')
    
    # Check if there are exactly 8 groups
    if len(groups) != 8:
        return False
    
    for group in groups:
        # Check if each group is a valid hexadecimal number
        try:
            # Use int() function with base 16 to convert the group to decimal
            decimal = int(group, 16)
            # Check if the decimal number is between 0 and 65535 (2^16 - 1)
            if decimal < 0 or decimal > 65535:
                return False
        except ValueError:
            return False
    
    return True