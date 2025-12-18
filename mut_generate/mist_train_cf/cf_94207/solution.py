"""
QUESTION:
Write a function named `compare_strings` that compares two input strings and returns the longer one. The function should be able to handle strings of up to 1 million characters and must have a time complexity of O(n), where n is the length of the longer string.
"""

def compare_strings(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    min_len = min(len1, len2)

    for i in range(min_len):
        if string1[i] != string2[i]:
            return string1 if len1 > len2 else string2

    return string1 if len1 >= len2 else string2