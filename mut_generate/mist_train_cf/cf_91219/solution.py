"""
QUESTION:
Create a function called `remove_vowels` that takes a sentence as input and returns the sentence with all vowels removed. The function should handle sentences containing punctuation marks and special characters. The vowels to be removed are 'a', 'e', 'i', 'o', 'u', and their uppercase counterparts.
"""

def remove_vowels(sentence):
    vowels = 'aeiouAEIOU'
    result = ''
    for char in sentence:
        if char not in vowels:
            result += char
    return result