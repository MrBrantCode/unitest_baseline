"""
QUESTION:
Write a function `utf8_encode_unicode` to take a string of Unicode characters as input and return the corresponding UTF-8 encoded byte sequence in the range of 0 to 255 in big-endian format.
"""

def utf8_encode_unicode(s):
    return s.encode('utf-8')