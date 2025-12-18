"""
QUESTION:
Implement a function named `compare_strings` that takes two string parameters and returns "yes" if the strings are equal, and "no" otherwise. The function should be case-sensitive, handle whitespace characters and punctuation marks, and support different character encodings. The function must not use built-in string comparison functions or methods, and its time complexity should not exceed O(n), where n is the length of the longer string.
"""

def compare_strings(string1, string2):
    if len(string1) != len(string2):  # If the lengths are different, the strings are not equal
        return "no"

    for i in range(len(string1)):
        if string1[i] != string2[i]:  # If any characters are different, the strings are not equal
            return "no"

    return "yes"