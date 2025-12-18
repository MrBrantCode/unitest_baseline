"""
QUESTION:
Write a function `count_distinct_words` that takes a string as input and returns a tuple containing the number of distinct words and a list of the most frequently occurring words in the string, sorted in descending order of frequency. The function should ignore any punctuation or special characters, treat uppercase and lowercase letters as distinct words, and exclude the stop words ["is", "the"] from the list of most frequent words. The function should have a time complexity of O(n) and a space complexity of O(m), where n is the length of the string and m is the number of distinct words.
"""

import re
from collections import Counter

def count_distinct_words(s):
    # Remove punctuation and special characters
    s = re.sub(r'[^\w\s]', '', s)
    
    # Convert string to lowercase and split into words
    words = s.lower().split()
    
    # Count the frequency of each word
    word_counts = Counter(words)
    
    # Remove stop words from word_counts
    stop_words = ["is", "the"]
    for stop_word in stop_words:
        if stop_word in word_counts:
            del word_counts[stop_word]
    
    # Sort word_counts by frequency in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Extract the distinct words and their frequencies
    distinct_words = [word[0] for word in sorted_word_counts]
    
    return len(distinct_words), distinct_words