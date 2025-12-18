"""
QUESTION:
Create a function named `word_frequency` that takes a string of text as input. The function should return a list of unique words and their frequencies in descending order, ignoring punctuation and treating words in a case-insensitive manner. If multiple words have the same frequency, they should be sorted alphabetically.
"""

def word_frequency(text):
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text).lower()
    words = text.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    return sorted(word_freq.items(), key=lambda x: (-x[1], x[0]))