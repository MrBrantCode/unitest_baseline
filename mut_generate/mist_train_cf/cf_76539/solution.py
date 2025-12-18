"""
QUESTION:
Create a function called `are_anagrams` that takes two string parameters, `str1` and `str2`, and returns a boolean value indicating whether the two input strings are anagrams of each other. The function should consider the sequences as case sensitive and should not modify the original input strings.
"""

def are_anagrams(str1, str2):
    # Convert the strings to lists of characters, sort them and compare
    return sorted(list(str1)) == sorted(list(str2))