"""
QUESTION:
Create a function `is_palindrome_vowels(string)` that checks if a given string is a palindrome and contains all the vowels (a, e, i, o, u) in alphabetical order. The function should be case-insensitive and ignore non-alphabetic characters. It should return `True` if the string is a palindrome and contains all vowels in alphabetical order, and `False` otherwise.
"""

def is_palindrome_vowels(string):
    string = string.lower()
    if string == string[::-1]:
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_order = []
        for char in string:
            if char in vowels and char not in vowel_order:
                vowel_order.append(char)
                if vowel_order != sorted(vowel_order):
                    return False
        return len(vowel_order) == len(vowels)
    return False