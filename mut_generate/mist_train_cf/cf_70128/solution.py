"""
QUESTION:
Create a function named `extract_words` that takes a string as input, extracts unique words containing the character 'a', and returns them as a comma-separated string in alphabetical order (case-insensitive). The function should ignore punctuation and white spaces, and handle edge cases where the input string may contain multiple spaces, punctuation, or words without the character 'a'. The function should also ensure that each word is only counted once, regardless of how many times it appears in the input string.
"""

import re
import string

def extract_words(input_string):
    input_string = re.sub('['+string.punctuation+']', '', input_string).lower()
    words = input_string.split()
    unique_words = set()

    for word in words:
        if 'a' in word:
            unique_words.add(word)

    unique_words = sorted(list(unique_words))
    return ', '.join(unique_words)