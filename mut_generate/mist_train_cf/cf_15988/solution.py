"""
QUESTION:
Write a function `count_words` that takes a sentence as input and returns the total number of words that contain at least one vowel and start with a consonant, ignoring any vowels that occur within a word that starts with a vowel. The function should be case-insensitive and consider 'a', 'e', 'i', 'o', and 'u' as vowels.
"""

def count_words(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0

    for word in sentence.split():
        if word[0].lower() not in vowels:
            has_vowel = any(char.lower() in vowels for char in word[1:])
            if has_vowel:
                count += 1

    return count