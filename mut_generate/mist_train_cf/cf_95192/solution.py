"""
QUESTION:
Write a function `check_vowels` that takes a sentence as input and returns `True` if all vowels in the sentence are followed by a consonant that is not 'y', and `False` otherwise. The function should be case-insensitive and ignore spaces in the sentence.
"""

def check_vowels(sentence):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxz'

    sentence = sentence.lower()
    sentence = sentence.replace(' ', '')  # remove spaces

    for i in range(len(sentence) - 1):
        if sentence[i] in vowels:
            if sentence[i+1] not in consonants or sentence[i+1] == 'y':
                return False

    return True