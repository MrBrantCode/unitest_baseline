"""
QUESTION:
Implement a function named `is_valid_ipv4_address` that determines whether a given string is a valid IPv4 address. The function should take a string `s` as input and return a boolean value. A valid IPv4 address should have exactly 4 octets separated by periods, with each octet being an integer between 0 and 255 (inclusive), and not have leading zeros. Additionally, the address should not be all zeros or all 255s. The function should ignore any leading or trailing spaces in the input string.
"""

def is_valid_ipv4_address(s):
    # Remove leading and trailing spaces
    s = s.strip()

    # Split the string by periods to get octets
    octets = s.split('.')

    # Check if the number of octets is exactly 4
    if len(octets) != 4:
        return False

    # Check each octet
    for octet in octets:
        # Check for empty or leading zeros
        if octet == '' or octet[0] == '0' and len(octet) > 1:
            return False

        try:
            # Convert octet to integer
            value = int(octet)
        except ValueError:
            return False

        # Check if the octet is between 0 and 255
        if value < 0 or value > 255:
            return False

    # Check if all octets are not all 0 or all 255
    if all(octet == '0' for octet in octets) or all(octet == '255' for octet in octets):
        return False

    # All checks passed
    return True