"""
QUESTION:
Create a function named `longest_common_prefix` that takes two string parameters, `str1` and `str2`. The function should find and return the longest common prefix of the two input strings, ignoring any non-alphanumeric characters and treating uppercase and lowercase letters as equal. The input strings are guaranteed to have at least 3 characters.
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