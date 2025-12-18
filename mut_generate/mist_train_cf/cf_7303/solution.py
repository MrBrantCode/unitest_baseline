"""
QUESTION:
Write a function `find_kth_most_frequent_word(s, k)` that finds the kth most frequent word with a length of at least 5 characters in a given string `s`. The function should return the word if it exists; otherwise, return `None`. Assume the string `s` can contain any printable ASCII characters. The words in the string are separated by spaces and punctuation marks are considered part of the words.
"""

from collections import defaultdict

def find_kth_most_frequent_word(s, k):
    word_freq = defaultdict(int)
    words = s.split()
    for word in words:
        if len(word) >= 5:
            word_freq[word] += 1
    sorted_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    if k <= len(sorted_freq):
        return sorted_freq[k-1][0]
    else:
        return None