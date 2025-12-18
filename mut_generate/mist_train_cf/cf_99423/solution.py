"""
QUESTION:
Write a function `is_valid_ipv4(ip_address)` that takes a string `ip_address` representing an IP address in IPv4 format and returns a boolean value indicating whether it is valid or not. The function should check that the IP address consists of four numbers separated by periods, each number is between 0 and 255 inclusive, leading zeros are not allowed, and no other characters except digits and periods are allowed. The function should also determine the class of the IP address (A, B, C, D, or E) based on the first octet.
"""

def is_valid_ipv4(ip_address):
    octets = ip_address.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        if octet.startswith('0') and len(octet) > 1:
            return False
        if int(octet) < 0 or int(octet) > 255:
            return False
    if ip_address.endswith('.'):
        return False
    first_octet = int(octets[0])
    if first_octet >= 1 and first_octet <= 126:
        return 'Class A'
    elif first_octet >= 128 and first_octet <= 191:
        return 'Class B'
    elif first_octet >= 192 and first_octet <= 223:
        return 'Class C'
    elif first_octet >= 224 and first_octet <= 239:
        return 'Class D'
    elif first_octet >= 240 and first_octet <= 255:
        return 'Class E'
    else:
        return 'Unknown class'