"""
QUESTION:
Create a function named `word_frequency` that takes a string of text as input and returns a list of words along with their frequencies. The function should ignore punctuation marks, be case-insensitive, and sort the output in descending order based on frequency.
"""

def word_frequency(text):
    # Remove punctuation and convert text to lowercase
    text = text.lower().replace('.', '').replace(',', '').replace('!', '').replace('?', '')
    words = text.split()
    
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Sort the word frequencies in descending order
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_count