"""
QUESTION:
Implement a function `do_it(hex_str)` that takes a valid hexadecimal string as input, converts it to its binary representation, and returns the corresponding ASCII string after decoding the binary representation. The function should return the decoded ASCII string.
"""

from binascii import unhexlify

def do_it(hex_str: str) -> str:
    binary_str = unhexlify(hex_str)  
    ascii_str = binary_str.decode('utf-8')  
    return ascii_str