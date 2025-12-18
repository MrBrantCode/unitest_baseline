"""
QUESTION:
Count the occurrences of a given word in a text while ignoring case sensitivity. The word should not be part of any other word. The function should be able to handle cases where the given word appears multiple times in a single word and should be efficient for large texts. Create a function called `count_occurrences` that takes two parameters: `text` and `word`, and returns the number of occurrences of the word in the text.
"""

import re

def count_occurrences(text, word):
    # Convert the text and word to lowercase for case insensitivity
    text = text.lower()
    word = word.lower()

    # Create a regular expression pattern to match the word as a standalone word
    pattern = r"\b{}\b".format(re.escape(word))

    # Use regex findall function to find all occurrences of the word in the text
    occurrences = re.findall(pattern, text)

    # Count the number of occurrences
    count = len(occurrences)
    
    return count