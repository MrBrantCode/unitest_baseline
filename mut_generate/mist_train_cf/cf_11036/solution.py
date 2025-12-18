"""
QUESTION:
Create a function named `is_valid_ipv6` that checks whether a given string represents a valid IPv6 address. The function should return `True` if the string is a valid IPv6 address and `False` otherwise. A valid IPv6 address consists of 8 groups of hexadecimal numbers separated by colons, and each group must be a hexadecimal number between 0 and 65535 (inclusive). Leading zeros are allowed in each group, but there must not be any extra or missing groups.
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