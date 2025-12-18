"""
QUESTION:
Implement a function `guidToBinary` that takes a string representing a GUID (Globally Unique Identifier) in the form of 8-4-4-4-12 hexadecimal digits grouped by hyphens and returns its binary representation as bytes. The GUID string is 36 characters long, consisting of 32 hexadecimal digits and 4 hyphens.
"""

def guidToBinary(guid_str):
    hex_str = guid_str.replace("-", "")  # Remove hyphens from the GUID string
    hex_bytes = bytes.fromhex(hex_str)  # Convert the hexadecimal string to bytes
    return hex_bytes