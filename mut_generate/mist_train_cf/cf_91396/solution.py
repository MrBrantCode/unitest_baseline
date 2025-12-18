"""
QUESTION:
Given a list of n strings and an integer k, implement a function `find_k_most_frequent_words(words, k)` that returns the k most frequent words in the list. If multiple words have the same frequency, return them in lexicographical order.
"""

def find_k_most_frequent_words(words, k):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return sorted(word_count.keys(), key=lambda x: (-word_count[x], x))[:k]