"""
QUESTION:
Create a function called `get_odd_unicode_chars` that takes a string as input and returns a list of characters in the string with odd Unicode values.
"""

def get_odd_unicode_chars(s):
    return [char for char in s if ord(char) % 2 != 0]