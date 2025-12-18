"""
QUESTION:
Write a function called `remove_vowels` that takes a string as input and returns a new string with all vowels (both lowercase and uppercase) removed, while maintaining the original string's punctuation and formatting.
"""

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return s.translate({ord(v): None for v in vowels})