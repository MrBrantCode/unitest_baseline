"""
QUESTION:
Define a function named `is_valid_ipv6` that takes a string `ip_str` as input and returns a boolean indicating whether it is a valid IPv6 address. The function should check the following conditions:
 
- The address should not start or end with a colon.
- The address should not contain consecutive colons (::) in the middle of the address, but can have one double colon in the entire address.
- The address should not contain more than 8 groups of hexadecimal digits.
- The address should not contain any non-hexadecimal characters other than colons.
- The address should not contain any lowercase letters.
- Each group of hexadecimal digits should be within the range of 0000 to FFFF.
- Each group should not contain leading or trailing zeros.
- Each group should not contain consecutive zeros.
- Each group should not be empty.
- Each group should have exactly 4 hexadecimal digits, unless abbreviated by using double colons (::).
"""

def is_valid_ipv6(ip_str):
    groups = ip_str.split(':')
    
    # Check for leading or trailing colons
    if ip_str[0] == ':' or ip_str[-1] == ':':
        return False
    
    # Check for consecutive colons
    if '::' in ip_str:
        if ip_str.count('::') > 1:
            return False
        if groups[0] == '':
            groups.pop(0)
        if groups[-1] == '':
            groups.pop(-1)
    
    # Check for more than 8 groups
    if len(groups) > 8:
        return False
    
    # Check for non-hexadecimal characters
    for group in groups:
        if not all(char.isdigit() or char.upper() in 'ABCDEF' for char in group):
            return False
    
    # Check for lowercase letters
    for group in groups:
        if any(char.islower() for char in group):
            return False
    
    # Check for consecutive zeros, empty groups, groups with more than 4 digits,
    # groups with less than 4 digits, groups with leading zeros, and groups with trailing zeros
    for group in groups:
        if group == '':
            return False
        if group.count('0') > 1:
            return False
        if len(group) > 4 or len(group) < 4:
            return False
        if group[0] == '0' and len(group) > 1:
            return False
        if group[-1] == '0' and len(group) > 1:
            return False
    
    return True