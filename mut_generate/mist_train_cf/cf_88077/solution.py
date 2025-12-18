"""
QUESTION:
Implement a case-sensitive function named `compare_strings` that compares two input strings character by character. The function should return "yes" if the strings are equal and "no" otherwise. It should handle whitespace characters, punctuation marks, special characters, and different character encodings, such as ASCII, UTF-8, or Unicode. The function should not use any built-in string comparison functions or methods and should have a time complexity not exceeding O(n), where n is the length of the longer string.
"""

def compare_strings(string1, string2):
    if len(string1) != len(string2):  # If the lengths are different, the strings are not equal
        return "no"

    for i in range(len(string1)):
        if string1[i] != string2[i]:  # If any characters are different, the strings are not equal
            return "no"

    return "yes"