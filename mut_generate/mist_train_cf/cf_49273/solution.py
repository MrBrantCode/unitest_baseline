"""
QUESTION:
Create a function `is_palindrome_vowels(string)` that takes a string as input, determines whether it is a palindrome and contains all the vowels in the English language (a, e, i, o, u) in a case-insensitive manner, ignoring non-alphabetic characters.
"""

def is_palindrome_vowels(string):
    vowels = set("aeiou")
    stripped_string = ''.join(ch for ch in string if ch.isalpha()).lower()
    string_vowels = set(ch for ch in stripped_string if ch in vowels)
    return stripped_string == stripped_string[::-1] and string_vowels == vowels