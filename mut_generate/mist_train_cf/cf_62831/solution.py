"""
QUESTION:
Write a function `is_all_numeric(s)` that takes a string `s` as input and returns `True` if all characters in the string are numeric, and `False` otherwise. The function should consider a string as numeric if it represents a signed decimal number, including negative numbers and numbers with a single decimal point. If the input is not a string, the function should return `False`.
"""

def is_all_numeric(s):
    try:
        if s == '':
            return False
        elif s.replace('.','',1).replace('-','',1).isdigit():
            return True
        else:
            return False
    except AttributeError:
        return False