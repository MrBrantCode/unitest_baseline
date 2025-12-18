"""
QUESTION:
Write a function `find_top_10_common_words(string)` that takes a string as input and returns the top 10 most common words excluding common stop words like "the", "and", "a", "is", etc. The function should have a time complexity of O(n), where n is the length of the input string.
"""

from collections import Counter

def find_top_10_common_words(string):
    stop_words = ["the", "and", "a", "is"]  # Add more stop words as needed

    words = string.lower().split()
    filtered_words = [word for word in words if word.lower() not in stop_words]
    word_counts = Counter(filtered_words)
    return word_counts.most_common(10)