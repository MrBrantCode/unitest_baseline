"""
QUESTION:
Capitalize all letters in the given string and reverse the order of the words, while removing all vowels from the string.

Create a function called `remove_vowels_and_reverse_words` that takes a string as input and returns the modified string.
"""

def remove_vowels_and_reverse_words(s):
    vowels = 'aeiouAEIOU'
    s = ''.join([c for c in s if c not in vowels])
    s = s.upper()
    s = ' '.join(s.split()[::-1])
    return s