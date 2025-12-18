"""
QUESTION:
Write a function `is_valid_ipv6_address` that takes a string `address` as input and returns `True` if it's a valid IPv6 address, and `False` otherwise. The function should ignore leading and trailing whitespace characters in the input string. A valid IPv6 address consists of exactly 8 parts separated by colons, where each part is a hexadecimal number between 0 and FFFF (inclusive).
"""

def is_valid_ipv6_address(address):
    # Remove leading and trailing whitespace characters
    address = address.strip()
    
    # Check if the address is a valid IPv6 address
    try:
        parts = address.split(':')
        
        # Must have exactly 8 parts
        if len(parts) != 8:
            return False
        
        for part in parts:
            # Each part must be a hexadecimal number between 0 and FFFF
            if not part or not part.isalnum() or int(part, 16) > 0xFFFF:
                return False
                
        return True
    
    except ValueError:
        return False