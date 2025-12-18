"""
QUESTION:
Create a function `has_o_second_last` that takes a list of words as input and returns `True` if any word (excluding palindromes) has 'o' as its second last character, and `False` otherwise. The function should not use any built-in Python functions.
"""

def has_o_second_last(lst):
    for word in lst:
        if word == word[::-1]:
            continue
        elif word[-2] == 'o':
            return True
    return False