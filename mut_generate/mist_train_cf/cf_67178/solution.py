"""
QUESTION:
Write a function `check_uppercase_and_count` that takes a string `moniker` as input and returns `True` if the string consists solely of uppercase alphabetic characters and its length is exactly 7, otherwise returns `False`.
"""

def check_uppercase_and_count(moniker):
    if moniker.isupper() and len(moniker) == 7 and moniker.isalpha():
        return True
    return False