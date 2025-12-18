"""
QUESTION:
Create a function `has_uncommon_unicode_chars` that takes a string as input and returns `True` if the string contains any Unicode characters outside the ASCII range (decimal Unicode code points greater than 127) and `False` otherwise.
"""

def has_uncommon_unicode_chars(input_string):
    for char in input_string:
        if ord(char) > 127:
            return True
    return False