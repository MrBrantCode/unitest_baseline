"""
QUESTION:
Create a function named `transform_text` that takes a string `text` as input and returns the transformed string. The function should convert all vowels in the text to uppercase, remove all punctuation marks except for periods and exclamation marks, and print the frequency of each word in descending order. Note that the input string should be pre-processed to lowercase before any transformations.
"""

import re
from collections import Counter

def transform_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Convert vowels to uppercase
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        text = text.replace(vowel, vowel.upper())

    # Remove all punctuation marks except for periods and exclamation marks
    text = re.sub(r'[^\w\s.!]', '', text)

    # Calculate the frequency of each word
    word_list = text.split()
    word_freq = Counter(word_list)

    # Print words along with their frequencies in descending order
    for word, freq in sorted(word_freq.items(), key=lambda x: x[1], reverse=True):
        print(word, freq)

    return text