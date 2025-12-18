"""
QUESTION:
Create a function named `word_frequency` that takes a string `text` as input. The function should return a list of unique words and their frequencies in the input text, sorted in descending order based on frequency. The comparison of words should be case-insensitive and punctuation marks should be ignored. A word is defined as a sequence of characters separated by spaces.
"""

def word_frequency(text):
    # Remove punctuation and convert text to lowercase
    text = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text).lower()
    
    # Split the text into words
    words = text.split()
    
    # Create a dictionary to store word frequencies
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort the word frequencies in descending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_freq