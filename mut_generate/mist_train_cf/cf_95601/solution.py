"""
QUESTION:
Write a function called `is_palindrome_vowels` that checks if a given string is a palindrome and contains all the vowels (a, e, i, o, u) in alphabetical order without any duplicates. The string must have a length greater than 5 characters. The function should be case-insensitive.
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