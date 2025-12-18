"""
QUESTION:
Create a function `convert_to_bytes` that takes a string `s` as input and returns its byte representation. The function should handle both ASCII and Unicode strings and return the byte representation of the input string in UTF-8 encoding.
"""

def convert_to_bytes(s: str) -> bytes:
    return s.encode('utf-8')