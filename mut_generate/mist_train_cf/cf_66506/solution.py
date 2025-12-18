"""
QUESTION:
Construct a function `check_pangram` that determines whether a given string is a pangram, containing all 26 letters of the alphabet, without utilizing any built-in set data structures or functions in Python. The function should return `True` if the string is a pangram and `False` otherwise. The function should be case-insensitive and ignore non-alphabet characters.
"""

def check_pangram(input_str):
    alpha_list = [False]*26
    for char in input_str:
        if not char.strip():
            continue
        index = ord(char.lower()) - ord('a')
        if 0 <= index < 26:
            alpha_list[index] = True
    for has_char in alpha_list:
        if not has_char:
            return False
    return True