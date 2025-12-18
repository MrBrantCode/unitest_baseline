"""
QUESTION:
Create a Python function named encode_non_ascii that takes a list of strings as input and returns a new list of strings where all non-ASCII characters (ASCII > 127) are replaced by their decimal Unicode equivalent, encoded by the form &#xXXXX; where XXXX is the utf8 code point of the character. The function should exclude digit characters within the input strings from the encoding process and only replace non-ASCII characters that are not part of any Python reserved words.
"""

import keyword
import re

def encode_non_ascii(strings):
    """
    Takes a list of strings and returns a new list of strings where all non-ASCII characters
    (ASCII > 127) are replaced by their decimal Unicode equivalent, encoded by the form &#xXXXX;
    where XXXX is the utf8 code point of the character. The function only replaces non-ASCII
    characters that are not part of any Python reserved words. The function also excludes any
    digit characters within the input strings from the encoding process.

    Args:
    - strings: list of strings

    Returns:
    - new_list: list of strings
    """

    # define pattern to match non-ASCII characters and digits
    pattern = re.compile("[^\x00-\x7F]|[0-9]")

    # define a dictionary to map non-ASCII characters to their Unicode equivalent
    replacements = {}
    for char in pattern.findall("".join(strings)):
        if ord(char) > 127 and char not in keyword.kwlist:
            replacements[char] = "&#x{:04x};".format(ord(char))

    # iterate over strings and encode non-ASCII characters
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