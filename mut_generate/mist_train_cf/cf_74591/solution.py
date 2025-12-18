"""
QUESTION:
Write a function `pickout_sequences` that takes a string as input and returns `True` if the string exhibits an alternating pattern of lowercase letters and special symbols, and `False` otherwise. The string should start with a lowercase letter and consist only of alternating lowercase letters and special symbols, where special symbols are any of the following: !, @, #, $, %, ^, &, *, (, ), [, ], -, _, +, =, ~, `. The input string will only contain these special symbols and lowercase letters.
"""

import re

def pickout_sequences(s):
    pattern = re.compile("^[a-z][!@#$%^&*()\[\]-_+=~`]{1}[a-z]([!@#$%^&*()\[\]-_+=~`]{1}[a-z])*$")
    if pattern.match(s):
        return True
    return False