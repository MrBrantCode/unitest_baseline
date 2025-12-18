"""
QUESTION:
Write a function `is_palindrome_vowels(string)` that checks if a given string is a palindrome, contains all the vowels (a, e, i, o, u) in alphabetical order without any duplicates, and has a length greater than 5 characters. The function should be case-insensitive, treating both lowercase and uppercase characters as valid vowels.
"""

def is_palindrome_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()
    string_vowels = sorted(set([char for char in string if char in vowels]))
    
    if len(string) <= 5:
        return False
    
    if string_vowels != vowels:
        return False
    
    return string == string[::-1]