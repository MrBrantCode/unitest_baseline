"""
QUESTION:
Write a function `count_distinct_words` that takes a string as input and returns the number of distinct words and a list of the most frequently occurring words (excluding the stop words "is" and "the") in the string, sorted in descending order of frequency. The function should ignore punctuation and special characters, and treat uppercase and lowercase letters as distinct words. It should have a time complexity of O(n), where n is the length of the string, and a space complexity of O(m), where m is the number of distinct words.
"""

import re
from collections import Counter

def count_distinct_words(string):
    # Remove punctuation and special characters
    string = re.sub(r'[^\w\s]', '', string)

    # Split string into words
    words = string.split()

    # Count the frequency of each word
    word_counts = Counter(words)

    # Remove stop words from word_counts
    stop_words = ["is", "the"]
    for stop_word in stop_words:
        if stop_word in word_counts:
            del word_counts[stop_word]

    # Get the number of distinct words
    num_distinct_words = len(word_counts)

    # Sort the most frequent words in descending order of frequency
    most_frequent_words = [word for word, count in word_counts.most_common()]

    return num_distinct_words, most_frequent_words