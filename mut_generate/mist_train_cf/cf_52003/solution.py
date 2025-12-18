"""
QUESTION:
Convert a given IP address in dot-decimal form to a 32-bit integer. Write a function `ip_to_int32` that takes a string representing an IP address as input and returns its corresponding 32-bit integer representation. The IP address will be in the format "xxx.xxx.xxx.xxx", where xxx is a value between 0 and 255.
"""

def ip_to_int32(ip):
    """
    Convert a given IP address in dot-decimal form to a 32-bit integer.

    Args:
        ip (str): IP address in the format "xxx.xxx.xxx.xxx", where xxx is a value between 0 and 255.

    Returns:
        int: The 32-bit integer representation of the IP address.
    """
    return sum(int(octet) << (24 - 8 * i) for i, octet in enumerate(ip.split('.')))