"""
QUESTION:
Implement a function `find_different_char_index` that returns the index of the first character different from the character at the current index `i` in a given array of characters `str`. Assume `str` is a null-terminated array and ignore out-of-bounds conditions. The function should compare adjacent characters in `str` without violating sequence point rules.
"""

def find_different_char_index(str):
    i = 0
    while i < len(str) - 1 and str[i] == str[i+1]:
        i += 1
    return i + 1 if i < len(str) - 1 else -1