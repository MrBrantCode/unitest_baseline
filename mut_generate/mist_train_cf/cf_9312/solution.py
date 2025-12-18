"""
QUESTION:
Write a function called `reorder_alphabetically` that takes a string `s` as input and returns the reordered string with characters sorted alphabetically. The function should consider the case of the letters while ordering them alphabetically, meaning uppercase letters come before lowercase letters.
"""

def reorder_alphabetically(s):
    sorted_string = sorted(s)
    return ''.join(sorted_string)