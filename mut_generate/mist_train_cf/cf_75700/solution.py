"""
QUESTION:
Write a function `get_signature(sig)` that takes a string input, converts each character to its ASCII representation, and returns the representations as a string of space-separated values. The input string should be obtained from the user.
"""

def get_signature(sig):
    ascii_version = [str(ord(c)) for c in sig]
    return ' '.join(ascii_version)