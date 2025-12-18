"""
QUESTION:
Create a function named `find_words` that finds all words in a given text that start with a specific character. The function should be case insensitive and able to exclude words containing specific character sequences. It should return a dictionary with the words as keys and their frequencies as values.

The function should take three parameters: `text` (the text to search in), `first_char` (the character that the words should start with), and `exclude` (a list of character sequences that should be excluded from the words). The `exclude` parameter should be optional and default to an empty list.
"""

import re
from collections import Counter

def find_words(text, first_char, exclude=[]):
    # Make the text lowercase
    text = text.lower()
    
    # Find all words that start with the first character
    words = re.findall(r'\b' + first_char.lower() + r'\w*', text)
    
    # Exclude certain words
    words = [word for word in words if all(ex not in word for ex in exclude)]
    
    # Calculate the frequency of each word
    freq = Counter(words)

    return freq