"""
QUESTION:
Implement a function named `compare_strings` that takes two string parameters `str1` and `str2` and returns "yes" if they are equal and "no" otherwise. The function should be case-sensitive and handle whitespace characters, punctuation marks, special characters, and different character encodings. It should not use any built-in string comparison functions or methods and have a time complexity of O(n), where n is the length of the longer string.
"""

def compare_strings(str1, str2):
    if len(str1) != len(str2):
        return "no"  # Strings have different lengths, they are different
    
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return "no"  # Found a mismatching character, strings are different
    
    return "yes"  # All characters match, strings are equal