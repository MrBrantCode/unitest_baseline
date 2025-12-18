"""
QUESTION:
Create a function `alternate_strings(string1, string2)` that takes two strings as input and returns a new string where the characters from `string1` and `string2` are alternated. If one string is longer than the other, append the remaining characters of the longer string to the end of the new string.
"""

def alternate_strings(string1, string2):
    new_string = ''
    length = min(len(string1), len(string2))
    for i in range(length):
        new_string += string1[i] + string2[i]
    if len(string1) > len(string2):
        new_string += string1[length:]
    elif len(string2) > len(string1):
        new_string += string2[length:]
    return new_string