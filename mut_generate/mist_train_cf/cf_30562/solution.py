"""
QUESTION:
Write a function `word_frequency(text)` that takes a string of text as input and returns the frequency of each word in the text, ignoring punctuation and considering words in a case-insensitive manner. The output should be a list of words along with their frequencies, sorted in descending order of frequency.
"""

def word_frequency(text):
    text = text.lower().replace('.', '').replace(',', '').replace('?', '').replace('!', '')
    words = text.split()
    
    frequency = {}
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_frequency