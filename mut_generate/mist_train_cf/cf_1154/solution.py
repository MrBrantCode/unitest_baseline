"""
QUESTION:
Implement the `is_substring` function to determine if one string is a substring of the other without using built-in string searching functions or libraries. The function should take two strings as input and return `True` if one string is a substring of the other, and `False` otherwise. The function should handle cases with empty strings, special characters, and strings of varying lengths (including very long strings). The time complexity of the function should be O(n+m), where n and m are the lengths of the two input strings.
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