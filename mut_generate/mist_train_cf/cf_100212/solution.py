"""
QUESTION:
Create a function `convert_strings_to_integers` that takes a list of strings representing integers in decimal, binary, or hexadecimal format, and returns a list of integers. The function should be able to automatically detect the base of each input string and convert it to an integer.
"""

def convert_strings_to_integers(str_list):
    return [int(s, 0) for s in str_list]