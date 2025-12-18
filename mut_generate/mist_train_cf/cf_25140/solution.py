"""
QUESTION:
Convert a 64-bit hexadecimal code address to a physical address in decimal form.

Write a function named `physical_address` that takes a 64-bit hexadecimal code address as input and returns its physical address in decimal form. The input will be a hexadecimal string prefixed with '0x'.
"""

def physical_address(hex_address):
    """
    Converts a 64-bit hexadecimal code address to a physical address in decimal form.

    Args:
    hex_address (str): A 64-bit hexadecimal code address prefixed with '0x'.

    Returns:
    int: The physical address in decimal form.
    """
    return int(hex_address, 16)