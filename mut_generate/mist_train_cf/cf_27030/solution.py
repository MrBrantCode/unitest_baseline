"""
QUESTION:
Write a function named `word_frequency` that takes a string of text as input, calculates the frequency of each word in a case-insensitive manner, and returns a list of unique words along with their respective frequencies in ascending order. Ignore punctuation marks and consider a word as a sequence of characters separated by spaces.
"""

def entrance(text):
    text = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    words = text.split()
    word_freq = {}
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return sorted(word_freq.items())