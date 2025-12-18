"""
QUESTION:
Create a function named `check_ip(ip)` that takes an IPv4 address string `ip` as input and returns a string describing whether it's a valid public IP address and its class (A, B, C, D, or E) or an invalid IP address. The function should exclude private IP address ranges.
"""

import re

def check_ip(ip):
    """
    Validate an IPv4 address string and return a string describing whether it's a valid public IP address and its class (A, B, C, D, or E) or an invalid IP address.
    
    Args:
    ip (str): The IPv4 address string to be validated.
    
    Returns:
    str: A string describing whether the IP address is valid public IP address and its class or an invalid IP address.
    """

    # Validate IP address using regex
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    
    if pattern.match(ip):
        # Check if IP address is private or not
        first_part = int(ip.split('.')[0])
        second_part = int(ip.split('.')[1])
        
        if first_part == 10 or (first_part == 172 and 16 <= second_part <= 31) or (first_part == 192 and second_part == 168):
            return "This is a private IP address."
        else:
            # Classify IP address
            if 1 <= first_part <= 126:
                return "This is a Class A IP address."
            elif 128 <= first_part <= 191:
                return "This is a Class B IP address."
            elif 192 <= first_part <= 223:
                return "This is a Class C IP address."
            elif 224 <= first_part <= 239:
                return "This is a Class D IP address."
            elif 240 <= first_part <= 254:
                return "This is a Class E IP address."
            else:
                return "This is an unknown IP address."
    else:
        return "Invalid IP address."