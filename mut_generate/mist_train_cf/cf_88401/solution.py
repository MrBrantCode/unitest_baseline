"""
QUESTION:
Write a function `compare_strings(string1, string2)` that compares two strings of equal length and returns the number of matching characters. The comparison should only consider alphabetic characters (both lowercase and uppercase) and ignore non-alphabetic characters. The function should return an error message if the input strings are not of equal length.
"""

import re

def compare_strings(string1, string2):
    if len(string1) != len(string2):
        return "Error: The lengths of the strings are not equal"

    count = 0
    for i in range(len(string1)):
        if re.match("^[a-zA-Z]+$", string1[i]) and re.match("^[a-zA-Z]+$", string2[i]):
            if string1[i] == string2[i]:
                count += 1
        else:
            continue

    return count