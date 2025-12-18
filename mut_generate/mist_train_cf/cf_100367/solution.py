"""
QUESTION:
Create a function `encode_non_ascii` that takes a list of strings as input and returns a new list of strings. The function should replace all non-ASCII characters (ASCII > 127) with their decimal Unicode equivalent in the form &#xXXXX; where XXXX is the utf8 code point of the character, excluding digits and non-ASCII characters that are part of Python reserved words.
"""

import keyword
import re

def encode_non_ascii(strings):
    pattern = re.compile("[^\x00-\x7F]|[0-9]")
    replacements = {}
    for char in pattern.findall("".join(strings)):
        if ord(char) > 127 and char not in keyword.kwlist:
            replacements[char] = "&#x{:04x};".format(ord(char))
    new_list = []
    for string in strings:
        new_string = ""
        for i, char in enumerate(string):
            if char in replacements:
                new_string += replacements[char]
            else:
                new_string += char
        new_list.append(new_string)
    return new_list