"""
QUESTION:
Create a function named `word_frequency` that takes a string of text as input, calculates the frequency of each word (defined as a sequence of characters separated by spaces, ignoring punctuation marks, and case-insensitive), and returns a list of unique words along with their frequencies, sorted in descending order based on frequency.
"""

def word_frequency(text):
    # Remove punctuation and convert text to lowercase
    text = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '').replace(';', '').replace(':', '')
    
    # Split the text into words
    words = text.split()
    
    # Create a dictionary to store word frequencies
    word_freq = {}
    
    # Count the frequency of each word
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # Sort the word frequencies in descending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_freq