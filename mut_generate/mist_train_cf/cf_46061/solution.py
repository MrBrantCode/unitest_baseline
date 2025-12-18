"""
QUESTION:
Create a function `check_mutual_palindromes(exp1, exp2)` that takes two string parameters `exp1` and `exp2` and returns `True` if both strings are palindromes (ignoring case, whitespace, and punctuation) and equal, and `False` otherwise.
"""

import string

def entrance(exp1, exp2):
    # remove punctuation
    exp1 = exp1.translate(str.maketrans('', '', string.punctuation))
    exp2 = exp2.translate(str.maketrans('', '', string.punctuation))
    # remove white spaces and convert to lower case
    exp1 = exp1.replace(" ", "").lower()
    exp2 = exp2.replace(" ", "").lower()
    # check if they are mutual palindromes
    return exp1 == exp1[::-1] and exp2 == exp2[::-1] and exp1 == exp2