"""
QUESTION:
Write a function `compare_word_sets(phrase1, phrase2)` that compares two input strings `phrase1` and `phrase2`, ignoring case and punctuation, to determine if they contain the same unique words. The function should return a boolean indicating whether the two phrases contain the same unique words, and also print the count of unique words in each phrase, the common words, and the unique words between them.
"""

import string

def compare_word_sets(phrase1: str, phrase2: str):
    # Remove punctuation, convert to lowercase and split strings into word lists
    phrase1_words = phrase1.translate(str.maketrans('', '', string.punctuation)).lower().split()
    phrase2_words = phrase2.translate(str.maketrans('', '', string.punctuation)).lower().split()

    # Convert lists to sets to remove duplicates and for faster comparison
    set1 = set(phrase1_words)
    set2 = set(phrase2_words)

    # Print counts
    print("First phrase unique word count: ", len(set1))
    print("Second phrase unique word count: ", len(set2))

    # Print common words
    print("Common words: ", set1.intersection(set2))

    # Print unique words
    print("Unique to first phrase: ", set1 - set2)
    print("Unique to second phrase: ", set2 - set1)

    return set1 == set2