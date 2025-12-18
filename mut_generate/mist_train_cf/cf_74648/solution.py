"""
QUESTION:
Write a function named `remove_vowels_digits_and_punctuation` that takes a string `text` as input and returns a new string that excludes vowels, digits, and punctuation marks, leaving only consonants.
"""

def remove_vowels_digits_and_punctuation(text):
    vowels = 'AEIOUaeiou'
    digits = '0123456789'
    punctuation = '!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~\n'

    result = ''
    for char in text:
        if char not in vowels and char not in digits and char not in punctuation:
            result += char

    return result