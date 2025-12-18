"""
QUESTION:
Compare two input strings and create a new string that contains all characters from both strings, excluding any characters that are present in both strings. The function should be named `compare_and_remove_letters`.
"""

def compare_and_remove_letters(string1, string2):
    result = ""
    for i in string1:
        if i not in string2:
            result += i
    for i in string2:
        if i not in string1:
            result += i
    return result