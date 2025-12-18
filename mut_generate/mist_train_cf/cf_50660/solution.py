"""
QUESTION:
Create a function named 'are_anagrams' that takes two alpha-numeric sequences (strings) as input and returns a boolean value indicating whether the two input sequences are lexical anagrams, ignoring case sensitivity and non-alphanumeric characters.
"""

def are_anagrams(str1, str2):
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()
    return sorted(str1) == sorted(str2)