"""
QUESTION:
Create a function `validate_ipv6_address` to determine whether a given string represents a valid IPv6 address. The function should be able to identify shortened forms of IPv6 addresses. If possible, construct a regular expression to match IPv6 addresses. The function should return `True` if the address is valid and `False` otherwise. Do not assume any specific input format other than the address string.
"""

import ipaddress

def validate_ipv6_address(address):
    try:
        ipaddress.IPv6Address(address)
        return True
    except ipaddress.AddressValueError:
        return False