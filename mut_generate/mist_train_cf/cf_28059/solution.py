"""
QUESTION:
Write a function `hex_to_ascii(hex_string: str) -> str` that takes a hexadecimal string as input, removes leading/trailing whitespaces and backslashes, decodes the string to bytes, and returns the corresponding ASCII representation, ignoring any non-ASCII characters. The input string may contain escaped hexadecimal characters.
"""

def hex_to_ascii(hex_string: str) -> str:
    # Remove any leading or trailing whitespace and backslashes
    hex_string = hex_string.strip().replace('\\', '')

    # Convert the hexadecimal string to bytes
    byte_string = bytes.fromhex(hex_string)

    # Decode the bytes to ASCII
    ascii_string = byte_string.decode('ascii', errors='ignore')

    return ascii_string