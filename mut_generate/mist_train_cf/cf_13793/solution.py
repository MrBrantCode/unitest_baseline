"""
QUESTION:
Create a function `is_valid_ipv4_address(ip_address)` that takes a string `ip_address` as input. The function should return `True` if `ip_address` is a valid IPv4 address and `False` otherwise. A valid IPv4 address consists of four numbers, each ranging from 0 to 255, separated by periods.
"""

def is_valid_ipv4_address(ip_address):
    parts = ip_address.split('.')
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255 or (len(part) > 1 and part[0] == '0'):
            return False
    
    return True