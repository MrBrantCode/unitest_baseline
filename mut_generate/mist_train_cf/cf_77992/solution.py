"""
QUESTION:
Implement a function called 'are_anagrams' that accepts two string arguments. The function should return a boolean indicating whether the two strings are anagrams of each other, i.e., whether one string can be rearranged into the other. The function should be case sensitive and consider whitespace and special characters as part of the strings.
"""

def are_anagrams(str1, str2):
    # Sort both strings
    str1 = sorted(str1)
    str2 = sorted(str2)

    # Compare sorted strings
    return str1 == str2