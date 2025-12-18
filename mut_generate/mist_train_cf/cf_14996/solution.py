"""
QUESTION:
Write a function `is_valid_ipv4(ip_address)` that determines if a given string `ip_address` is a valid IPv4 address. The function should return `True` if the string is a valid IPv4 address and `False` otherwise. The input string is a valid IPv4 address if it consists of exactly four parts separated by dots, and each part is a digit string that represents an integer between 0 and 255 inclusive.
"""

def is_valid_ipv4(ip_address):
    # Split the IP address into its components
    ip_components = ip_address.split('.')

    # Check if the IP address has exactly four components
    if len(ip_components) != 4:
        return False

    # Check if each component is a valid integer between 0 and 255
    for component in ip_components:
        try:
            value = int(component)
            if value < 0 or value > 255:
                return False
        except ValueError:
            return False

    return True