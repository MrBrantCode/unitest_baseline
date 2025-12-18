"""
QUESTION:
Implement a function `is_substring` that takes two strings `string1` and `string2` as input and returns `True` if one string is a substring of the other, and `False` otherwise. The function should not use any built-in string searching functions or libraries and should have a time complexity of O(n+m), where n and m are the lengths of the two input strings. The function should handle cases where the input strings are empty or have special characters.
"""

def is_substring(string1, string2):
    if string1 == '' or string2 == '':
        return False
    if string1 == string2:
        return True
    if len(string1) > len(string2):
        longer_string = string1
        shorter_string = string2
    else:
        longer_string = string2
        shorter_string = string1
    for i in range(len(longer_string) - len(shorter_string) + 1):
        if longer_string[i:i+len(shorter_string)] == shorter_string:
            return True
    return False