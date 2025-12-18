"""
QUESTION:
Create a function `word_count(sentence)` that takes a string `sentence` as input and returns a dictionary where each key is a unique word from the sentence and its corresponding value is the word's frequency in the sentence. The function should be case-insensitive and consider each word as a separate entity, regardless of its part of speech or grammatical function.
"""

def word_count(sentence):
    words = sentence.lower().split()  # Convert sentence into list of words
    word_dict = {}  # dictionary to store word:count pairs

    for word in words:
        if word in word_dict:  # If word is already in dictionary, increment its count
            word_dict[word] += 1
        else:  # If word is not in dictionary, add it with count 1
            word_dict[word] = 1

    return word_dict