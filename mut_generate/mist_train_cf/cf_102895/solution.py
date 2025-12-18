"""
QUESTION:
Create a function named `word_frequency` that takes a sentence as input, separates the words, and returns a list of tuples containing each word and its frequency in descending order of frequency. The input sentence should be case-sensitive, and punctuation should be treated as part of the word.
"""

def word_frequency(sentence):
    words = sentence.split()
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
    return sorted(word_count.items(), key=lambda x: x[1], reverse=True)