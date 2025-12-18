"""
QUESTION:
Write a function `string_to_hex` that takes an input string and returns its hexadecimal representation by converting each character to its ASCII value and then to hexadecimal, with each hexadecimal value separated by a colon.
"""

def string_to_hex(input_string):
    return ":".join("{:02x}".format(ord(c)) for c in input_string)