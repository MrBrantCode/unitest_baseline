"""
QUESTION:
Write a function called `is_valid_ipv4` that takes a string input representing an IP address in IPv4 format and returns a boolean value indicating whether it is valid or not. The function should check the following conditions: 
- The IP address should consist of four numbers separated by periods.
- Each number should be between 0 and 255, inclusive.
- Leading zeros are not allowed.
- Trailing periods are not allowed.
- No other characters except digits and periods are allowed in the input string. 
Also, print the class of the IP address (A, B, C, D, or E) based on the first octet. The IP address class is determined by the first octet as follows: 
- Class A: 1-126
- Class B: 128-191
- Class C: 192-223
- Class D: 224-239
- Class E: 240-255
"""

def entance(ip_address):
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
        print('Class A')
    elif first_octet >= 128 and first_octet <= 191:
        print('Class B')
    elif first_octet >= 192 and first_octet <= 223:
        print('Class C')
    elif first_octet >= 224 and first_octet <= 239:
        print('Class D')
    elif first_octet >= 240 and first_octet <= 255:
        print('Class E')
    else:
        print('Unknown class')
    return True