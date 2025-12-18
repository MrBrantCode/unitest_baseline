"""
QUESTION:
Implement `String#ipv4_address?`, which should return true if given object is an IPv4 address - four numbers (0-255) separated by dots.

It should only accept addresses in canonical representation, so no leading `0`s, spaces etc.
"""

from re import compile, match

# Regular expression to match a valid IPv4 address
REGEX = compile(r'^((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.){3}(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$')

def is_valid_ipv4_address(address: str) -> bool:
    """
    Check if the given string is a valid IPv4 address.

    Args:
        address (str): The string to be checked.

    Returns:
        bool: True if the string is a valid IPv4 address, otherwise False.
    """
    return bool(match(REGEX, address))