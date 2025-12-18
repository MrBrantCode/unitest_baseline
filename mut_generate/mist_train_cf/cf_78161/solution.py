"""
QUESTION:
Write a function named `address_classifier` that takes an IP address string as input. The function should return the type of IP address ('IPv4 Decimal', 'IPv4 Octal', or 'IPv6') if the address is valid, and False otherwise. The function should consider an IPv4 address to be in octal form if its first segment starts with a leading zero.
"""

import ipaddress

def address_classifier(address):
    try:
        ipaddr = ipaddress.ip_address(address)
        if isinstance(ipaddr, ipaddress.IPv4Address):
            if str(int(address.split(".", 1)[0])) != address.split(".", 1)[0]: 
                return 'IPv4 Octal'
            else:
                return 'IPv4 Decimal'
        else:
            return 'IPv6'
    except ValueError:
        return False