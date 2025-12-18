"""
QUESTION:
Write a function called `replace_digits` that takes two parameters: a string and a character. The function should replace all numerical digits in the string with the given character.
"""

def replace_digits(string, char):
    tran_tab = str.maketrans('0123456789', char * 10)
    return string.translate(tran_tab)