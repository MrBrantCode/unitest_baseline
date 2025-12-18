"""
QUESTION:
Write a function named `word_frequency(seq)` that takes a string `seq` as input, splits it into words using a hyphen as a delimiter, counts the frequency of each word, and returns the unique words in decreasing order of frequency. The function should consider the case of the words, treating 'Example' and 'example' as different words.
"""

from collections import Counter

def word_frequency(seq):
    words = seq.split('-')     # Split the sequence by hyphen to get the words
    word_count = Counter(words) # Use Counter from collections to count the frequency of each word

    # Convert the counter object to a list of (word, count) tuples
    # and sort it by the frequency in decreasing order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_word_count