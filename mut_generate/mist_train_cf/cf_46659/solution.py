"""
QUESTION:
Write a function `conv_uppercase_reverse_nondigit` that takes a string as input, converts it to uppercase, reverses the string, and removes any numerical digits. The function should return the modified string.
"""

def conv_uppercase_reverse_nondigit(s):
    return ''.join([i for i in s[::-1] if not i.isdigit()]).upper()