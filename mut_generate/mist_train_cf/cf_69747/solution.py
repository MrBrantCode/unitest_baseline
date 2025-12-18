"""
QUESTION:
Develop a function named `count_letters` that takes a list of words as input and returns the frequency of individual letters appearing in the list. The function should handle the following requirements:

- Handle capitalization and normalize special characters (like é, é) to their base forms (like e).
- Provide an error indication in situations where non-alphabetic characters are found.
- Handle non-string values in the list properly by printing an error message and continuing to the next element.

Restrictions:
- The function should handle Unicode characters and non-English alphabets.
- The function should ignore non-alphabetic characters in the words.
"""

import unicodedata
from collections import Counter

def count_letters(word_list):
    counts = Counter()
    for word in word_list:
        try:
            word = unicodedata.normalize('NFKD', word).encode('ASCII', 'ignore').decode() # Normalize and remove special characters
        except TypeError:
            print(f"Error: Non-string value {word} in list")
            continue
        for letter in word.lower():  # Normalize to lowercase
            if letter.isalpha():  # Check if character is a letter
                counts[letter] += 1
            else:
                print(f"Error: Non-alphabetical character '{letter}' in word '{word}'")
    return counts