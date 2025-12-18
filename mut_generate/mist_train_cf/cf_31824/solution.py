"""
QUESTION:
Implement a function `word_frequency` that takes a list of strings as input and returns a dictionary where the keys are the unique words in the input list and the values are the frequencies of those words. The function should ignore case sensitivity and consider words with different cases as the same word. The input list contains only strings. The function should return a dictionary with word frequencies.
"""

def word_frequency(words):
    frequency = {}
    for word in words:
        word = word.lower()
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency