"""
QUESTION:
Create a function named `split_string` that takes two parameters: a string and a length. The function should split the input string into chunks of the specified length and return them as a list of strings. The function should handle cases where the string length is not a multiple of the specified length by allowing the last chunk to be shorter.
"""

def split_string(s, n):
    return [s[i:i+n] for i in range(0, len(s), n)]