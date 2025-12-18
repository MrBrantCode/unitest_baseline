"""
QUESTION:
Create a function named `word_counter` that takes a string `sentence` as input. The function should return a dictionary where the keys are unique words from the sentence and the values are their corresponding frequencies. The function should be case-insensitive, consider punctuation as word boundaries, and sort the output in descending order of frequency. If two words have the same frequency, they should be sorted in alphabetical order.
"""

import string

def word_counter(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation)).lower()
    
    wordFrequency = {}
    words = sentence.split()
    for word in words:
        if word in wordFrequency:
            wordFrequency[word] += 1
        else:
            wordFrequency[word] = 1

    sorted_frequency = sorted(wordFrequency.items(), key=lambda x:(-x[1],x[0]))
    return dict(sorted_frequency)