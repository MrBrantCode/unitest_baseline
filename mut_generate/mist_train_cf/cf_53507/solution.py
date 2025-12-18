"""
QUESTION:
Write a function `find_max` that takes a list of distinct strings as input and returns the word with the highest quantity of individual characters. If multiple strings have the maximum count of unique characters, return the earliest one in lexicographical sequence.
"""

def find_max(words):
    words_with_counts = [(word, len(set(word))) for word in words]
    max_count = max(words_with_counts, key=lambda x: x[1])[1]
    max_words = [word for word, count in words_with_counts if count == max_count]
    return min(max_words)