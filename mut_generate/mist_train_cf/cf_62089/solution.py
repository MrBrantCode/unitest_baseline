"""
QUESTION:
Create a function called `swap_whitespace_and_underscore` that takes a string as input and returns the modified string where all whitespaces are replaced with underscores and all underscores are replaced with whitespaces.
"""

def swap_whitespace_and_underscore(string):
    to_swap = " _"
    swapped = "_ "
    trans_dict = str.maketrans(to_swap, swapped)
    return string.translate(trans_dict)