"""
QUESTION:
Create a function `analyze_text` that takes a string as input and returns a dictionary containing three values: 
- `word_count`: a dictionary where the keys are the unique words in the text (case insensitive) and the values are their respective frequencies,
- `anagrams`: a dictionary where the keys are tuples representing the sorted characters of the anagrams and the values are the number of distinct anagrams for each key,
- `palindromes`: a list of palindromes found in the text (case insensitive, length > 1).

The function should ignore punctuation, handle case insensitivity, and not consider a word as an anagram of itself.
"""

import collections
import re

def analyze_text(text):
    # Clean the text by making all words lower case and remove punctuation
    cleaned_text = re.sub('[^a-z\s]', '', text.lower())
    words = cleaned_text.split()

    word_counts = collections.Counter(words)
    anagrams = {}
    palindromes = set()

    for word in words:
        # Create a sorted tuple of characters to uniquely identify anagrams
        sorted_word_tuple = tuple(sorted(word))
        if sorted_word_tuple in anagrams:
            anagrams[sorted_word_tuple].add(word)
        else:
            anagrams[sorted_word_tuple] = {word}

        # Check if the word is a palindrome
        if word == word[::-1] and len(word) > 1:
            palindromes.add(word)

    # Create a dictionary to hold the results
    results = {
        'word_count': dict(word_counts),
        'anagrams': {k: len(v) - 1 for k, v in anagrams.items() if len(v) > 1},
        'palindromes': list(palindromes)
    }

    return results