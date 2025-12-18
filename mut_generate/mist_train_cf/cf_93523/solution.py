"""
QUESTION:
Write a function named `replace_adjacent_chars` that takes four parameters: a string and three characters (`char1`, `char2`, `replace_char`). The function should replace all occurrences of `char1` followed by `char2` or `char2` followed by `char1` in the given string with `replace_char`, while maintaining the original order of characters.
"""

def replace_adjacent_chars(string, char1, char2, replace_char):
    result = ""
    i = 0

    while i < len(string):
        # Check if the current character and the next character are equal to the characters to be replaced
        if i < len(string) - 1 and (string[i] == char1 and string[i+1] == char2) or (string[i] == char2 and string[i+1] == char1):
            result += replace_char
            i += 2  # Skip the next character since it has been replaced
        else:
            result += string[i]
            i += 1

    return result