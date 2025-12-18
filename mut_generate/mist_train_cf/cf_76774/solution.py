"""
QUESTION:
Create a function named `interlace_strings` that accepts two string inputs `str1` and `str2`. The function should return a new string that alternates characters from `str1` and `str2`. If one string is longer than the other, the remaining characters from the longer string should be appended to the end of the output string.
"""

def interlace_strings(str1, str2):
    result = ""
    length = min(len(str1), len(str2))
    for i in range(length):
        result += str1[i] + str2[i]
    return result + str1[length:] + str2[length:]