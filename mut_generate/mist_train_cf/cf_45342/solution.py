"""
QUESTION:
Create a function named `string_to_hex` that takes a string input and returns its hexadecimal encoding as a string, where each byte is represented in two hexadecimal digits and separated by a space.
"""

def string_to_hex(my_string):
    return " ".join("{:02x}".format(ord(c)) for c in my_string)