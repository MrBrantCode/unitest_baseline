"""
QUESTION:
Extract Unique Words from a Sentence

Write a function named `extract_unique_words` that takes a string sentence as input, removes any punctuation, converts all words to lowercase, and returns a list of unique words.

Restrictions: 
- Use the `string` module to access punctuation characters.
- The output should be a list of unique words in lowercase.
"""

import string

def extract_unique_words(sentence):
    """
    Extract unique words from a sentence.

    Args:
        sentence (str): Input sentence.

    Returns:
        list: A list of unique words in lowercase.
    """
    # Remove punctuation
    sentence = sentence.translate(str.maketrans("", "", string.punctuation))

    # Convert to lowercase
    sentence = sentence.lower()

    # Extract unique words and store them in a list
    unique_words = list(set(sentence.split()))

    return unique_words