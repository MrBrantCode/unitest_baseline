"""
QUESTION:
Implement a function `validate_ip(ip)` that determines whether the given string `ip` is a valid IP address. The function should differentiate between IPv4 and IPv6 addresses, and it must not use any built-in or external libraries for validation. 

The function should return 'IPv4' if the address is a valid IPv4 address, 'IPv6' if it is a valid IPv6 address, and `False` otherwise.
"""

def validate_ip(ip):
    # Separate the IP address
    if ("." in ip) and (":" not in ip):    # Potential IPv4
        parts = ip.split(".")
        if len(parts) != 4:    # Must be 4 sections
            return False
        for part in parts:
            if not part.isdigit():    # Must be numeric
                return False
            number = int(part)
            if number < 0 or number > 255:    # Must be in 0-255 range
                return False
        return 'IPv4'
    elif (":" in ip) and ("." not in ip):    # Potential IPv6
        parts = ip.split(":")
        if len(parts) > 8:    # Must be at most 8 sections
            return False
        for part in parts:
            if len(part) > 4:    # Each section is at most 4 digits
                return False
            if not all(c in "0123456789abcdefABCDEF" for c in part):    # All characters must be hexadecimal
                return False
        return 'IPv6'
    else:
        return False