"""
QUESTION:
Implement a function named `word_freq` that takes a string of text as input and returns a dictionary where the keys are the individual words from the text and the values are their corresponding frequencies. The function should consider each word as a case-sensitive string and should not ignore any punctuation. The input string may contain multiple spaces between words.
"""

def word_freq(text):
    word_freq = {}
    words = text.split()
    for word in words:
        if word in word_freq:
            word_freq[word] = word_freq[word] + 1
        else:
            word_freq[word] = 1
    return word_freq