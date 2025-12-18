"""
QUESTION:
Write a function named `remove_vowels(sentence)` that takes a string `sentence` as input and returns the modified string after removing all vowels. The function should preserve all non-alphabetic characters, including punctuation marks and special characters.
"""

def remove_vowels(sentence):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in sentence:
        if char not in vowels:
            result += char
    return result