"""
QUESTION:
Create a function called `are_anagrams` that takes two strings as input and returns a boolean value indicating whether the two input strings are anagrams of each other. The function should ignore the order of characters in the strings and consider only the characters themselves. For example, "listen" and "silent" should be considered anagrams.
"""

def are_anagrams(string1, string2):
    return sorted(string1) == sorted(string2)