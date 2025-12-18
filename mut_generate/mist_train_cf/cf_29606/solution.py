"""
QUESTION:
Implement a function `word_frequency` that takes a string `text` as input, and returns a list of tuples. Each tuple should contain a unique word from the text and its frequency, sorted in descending order of frequency. Consider a word as a sequence of non-whitespace characters.
"""

def word_frequency(text):
    word_list = text.split()
    word_count = {}
    
    for word in word_list:
        word_count[word] = word_count.get(word, 0) + 1
    
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_count