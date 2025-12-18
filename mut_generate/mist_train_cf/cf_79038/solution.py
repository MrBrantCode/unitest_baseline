"""
QUESTION:
Create a function named `check_anagram` that takes two string parameters. The function should determine whether the input strings are anagrams of each other, disregarding case and spaces. It should return `True` if the strings are anagrams, and `False` otherwise.
"""

def check_anagram(s1, s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)