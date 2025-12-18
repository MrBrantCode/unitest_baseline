"""
QUESTION:
Create a function named `is_anagram` that takes two strings `s1` and `s2` as arguments. The function should return `True` if the two strings are anagrams of each other (case-insensitive), the string which is a palindrome (case-insensitive) if the strings are not anagrams, or `False` if neither condition is satisfied.
"""

def is_anagram(s1, s2):
    def is_palindrome(s):
        return s.lower() == s.lower()[::-1]

    if sorted(s1.lower()) == sorted(s2.lower()):
        return True
    elif is_palindrome(s1):
        return s1
    elif is_palindrome(s2):
        return s2
    else:
        return False