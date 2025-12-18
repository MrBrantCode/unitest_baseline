"""
QUESTION:
Construct a function called `remove_letter` that takes two parameters: a string `my_string` and a single alphanumeric character `letter`. This function should return the string `my_string` with every occurrence of `letter` removed, preserving the original order of the remaining characters.
"""

def remove_letter(my_string, letter):
    return my_string.replace(letter, '')