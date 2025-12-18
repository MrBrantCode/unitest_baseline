"""
QUESTION:
Create a function called `word_frequency` that takes a string of text as input and returns a list of unique words along with their frequencies, sorted in descending order. The comparison of words should be case-insensitive, and punctuation marks should be disregarded. A word is defined as a sequence of characters separated by spaces.
"""

def word_frequency(text):
    # Remove punctuation and convert text to lowercase
    text = ''.join([c.lower() if c.isalpha() or c.isspace() else ' ' for c in text])
    
    # Split the text into words
    words = text.split()
    
    # Create a dictionary to store word frequencies
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Sort the word frequencies in descending order
    return sorted(word_freq.items(), key=lambda x: x[1], reverse=True)