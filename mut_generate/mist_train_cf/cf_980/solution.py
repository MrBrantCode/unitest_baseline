"""
QUESTION:
Write a function `count_words` that takes a sentence as input and returns the total number of words that start with a consonant and contain at least one vowel, ignoring any words that contain special characters or numbers.
"""

import re

def count_words(sentence):
    # Remove special characters and numbers
    sentence = re.sub('[^A-Za-z\s]', '', sentence)

    # Split the sentence into words
    words = sentence.split()

    count = 0
    vowels = set('aeiou')

    for word in words:
        if word[0].lower() not in vowels:  # Check if word starts with a consonant
            if any(char in vowels for char in word):  # Check if word contains at least one vowel
                count += 1

    return count