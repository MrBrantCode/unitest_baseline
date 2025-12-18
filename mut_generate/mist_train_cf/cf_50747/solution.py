"""
QUESTION:
Write a function `complex_palindrome_check(s)` that takes a string `s` as input and returns `True` if the string is a palindrome and contains all the vowels (a, e, i, o, u), and `False` otherwise. The function should be case-insensitive when checking for vowels.
"""

def complex_palindrome_check(s):
    # Check if string is the same backwards as forwards.
    palindrome_check = s == s[::-1]
    
    # Check if string has all vowels.
    vowels = set('aeiou')
    vowel_check = vowels.issubset(set(s.lower()))

    return palindrome_check and vowel_check