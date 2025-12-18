"""
QUESTION:
Create a function `longest_common_prefix(str1, str2)` that finds the longest common prefix of two input strings `str1` and `str2`, both with a length of at least 3 characters. The function should be case-insensitive, ignoring special characters and treating uppercase and lowercase letters as equal when comparing the strings.
"""

import re

def longest_common_prefix(str1, str2):
    # Convert strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove special characters
    str1 = re.sub('[^a-zA-Z0-9]', '', str1)
    str2 = re.sub('[^a-zA-Z0-9]', '', str2)

    # Find the length of the shorter string
    length = min(len(str1), len(str2))

    # Compare characters in the same position of both strings
    result = ""
    for i in range(length):
        if str1[i] == str2[i]:
            result += str1[i]
        else:
            break

    return result