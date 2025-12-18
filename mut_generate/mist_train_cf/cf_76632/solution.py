"""
QUESTION:
Design a function `are_anagrams` that takes two string inputs and returns a boolean value indicating whether they are anagrams of each other, ignoring case sensitivity, white spaces, and punctuation. The function should handle strings containing special characters and should not be limited to single-word inputs.
"""

def are_anagrams(string1, string2):
    # Removing all non-letter characters and converting to lower case
    string1 = ''.join(e for e in string1 if e.isalpha()).lower()
    string2 = ''.join(e for e in string2 if e.isalpha()).lower()

    # If both strings have the same length, the sorted strings are also identical
    return sorted(string1) == sorted(string2)