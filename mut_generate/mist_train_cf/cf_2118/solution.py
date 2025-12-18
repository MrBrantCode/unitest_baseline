"""
QUESTION:
Implement a function `replace_char` that takes a string `str`, a character `old_char`, and a character `new_char` as input. The function should replace all occurrences of `old_char` in `str` with `new_char` if `old_char` is not immediately followed by a whitespace character or if it is the last character in `str`. The input string `str` has a maximum length of 1000 characters. The function should not use built-in string manipulation functions or regular expressions, only basic string operations and loops. Return the modified string.
"""

def replace_char(s, old_char, new_char):
    modified_str = ""
    i = 0
    while i < len(s):
        if s[i] == old_char:
            if i == len(s) - 1 or (i < len(s) - 1 and s[i + 1] == ' '):
                modified_str += new_char
            else:
                modified_str += s[i]
        else:
            modified_str += s[i]
        i += 1
    return modified_str