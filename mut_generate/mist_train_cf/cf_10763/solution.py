"""
QUESTION:
Write a function named `compare_strings` that takes two parameters `string1` and `string2`. This function should compare two strings and determine their alphabetical order without using built-in string comparison functions or methods. It should return the string that comes first alphabetically. If the strings are equal, it can return either string. The function should handle strings of different lengths.
"""

def compare_strings(string1, string2):
    i = 0

    while i < len(string1) and i < len(string2):
        if string1[i] > string2[i]:
            return string2
        elif string1[i] < string2[i]:
            return string1
        else:
            i += 1

    if len(string1) < len(string2):
        return string1
    else:
        return string2