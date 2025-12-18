"""
QUESTION:
Create a function named `word_frequency` that takes a string as input. The function should return a dictionary containing the frequency of each word in the string, considering words as case-sensitive and excluding any words that contain numbers or special characters.
"""

def word_frequency(string):
    word_freq = {}

    words = string.split()

    for word in words:
        if not any(char.isdigit() or not char.isalpha() for char in word):
            word_freq[word] = word_freq.get(word, 0) + 1

    return word_freq