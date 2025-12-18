"""
QUESTION:
Create a function named `unique_concat` that takes two strings as input and returns their concatenation with unique characters. The order of characters in the output string should be the order of their first appearance in the concatenated string.
"""

def unique_concat(str1, str2):
    concat_str = str1 + str2
    unique_chars = set()
    for char in concat_str:
        unique_chars.add(char)
    unique_concat_str = ''.join(sorted(unique_chars, key=concat_str.index))
    return unique_concat_str