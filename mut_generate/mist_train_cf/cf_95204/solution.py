"""
QUESTION:
Implement a function named `compare_strings` that takes two strings `str1` and `str2` as input and returns "yes" if they are equal, and "no" otherwise. The comparison should be case-sensitive and should handle whitespace characters, punctuation marks, special characters, and different character encodings. The function should not use any built-in string comparison functions or methods, and its time complexity should not exceed O(n), where n is the length of the longer string.
"""

def compare_strings(str1, str2):
    if len(str1) != len(str2):
        return "no"  # Strings have different lengths, they are different
    
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return "no"  # Found a mismatching character, strings are different
    
    return "yes"  # All characters match, strings are equal