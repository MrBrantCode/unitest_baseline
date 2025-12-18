"""
QUESTION:
Define a function `find_max` that accepts a list of unique string inputs and returns the word with the most distinct characters, ignoring case. If multiple words have the same unique character count, return the first word alphabetically. The function should run in O(n) time complexity, where n is the total number of characters across all words.
"""

def find_max(words):
    max_unique_count = 0
    max_word = None

    for word in words:
        unique_count = len(set(word.lower()))
        
        if unique_count > max_unique_count:
            max_unique_count = unique_count
            max_word = word
        elif unique_count == max_unique_count:
            max_word = min(word, max_word)

    return max_word