"""
QUESTION:
Create a function `validate_ip` that takes an IP address as a string and determines whether it's a valid IPv4 or IPv6 address. If the IP is valid, return "Valid IPv4" or "Valid IPv6". If it's not a valid IP, return "Invalid IP address". The function should validate IPv6 addresses according to the standard notation.
"""

import ipaddress

def validate_ip(ip_address):
    try:
        if ipaddress.ip_address(ip_address).version == 4:
            return "Valid IPv4"
        elif ipaddress.ip_address(ip_address).version == 6:
            return "Valid IPv6"
    except ValueError:
        return "Invalid IP address"