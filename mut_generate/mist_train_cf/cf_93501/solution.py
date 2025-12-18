"""
QUESTION:
Write a function `find_most_frequent_word` that takes a string `sentence` as input and returns the word that has the maximum frequency in the string. If multiple words have the same maximum frequency, return the word that occurs first in the string. The function should be case-insensitive.
"""

def find_most_frequent_word(sentence):
    sentence = sentence.lower()
    words = sentence.split()
    word_freq = {}
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    max_freq = 0
    most_frequent_word = None

    for word, freq in word_freq.items():
        if freq > max_freq:
            max_freq = freq
            most_frequent_word = word

    return most_frequent_word