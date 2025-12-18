"""
QUESTION:
Create a function named `is_palindrome_with_vowels` that determines if a given string is a palindrome and contains all English vowels ('a', 'e', 'i', 'o', 'u'). The function should be case-insensitive and disregard non-alphabetical characters.
"""

def is_palindrome_with_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str = ''
    s = s.lower()   # switch to lowercase
    for char in s:
        if char.isalpha():  # if character is in alphabet
            str += char
            if char in vowels:
                vowels.remove(char)  # remove vowel from list
    if len(vowels) != 0:  # check if all vowels are met
        return False
    return str == str[::-1]  # Compare the original and reversed string