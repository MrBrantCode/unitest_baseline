"""
QUESTION:
Write a function called `are_anagrams` that takes two string arguments. The function should return `True` if the strings are anagrams of each other (ignoring case differences) and `False` otherwise.
"""

def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    return sorted(str1) == sorted(str2)