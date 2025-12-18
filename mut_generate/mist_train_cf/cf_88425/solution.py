"""
QUESTION:
Write a function named `process_list` that takes a list of words and numbers as input and returns three values: a list of unique words, a list of unique numbers, and a dictionary of word frequencies. The function should handle case sensitivity when identifying unique words and remove punctuation marks from the words. It should also be able to handle any number of lists as input.
"""

import string

def process_list(words):
    unique_words = []
    unique_numbers = []
    word_frequency = {}

    def remove_punctuation(word):
        # Remove punctuation marks from the word
        return word.translate(str.maketrans('', '', string.punctuation))

    for word in words:
        word = remove_punctuation(word)

        if word.isnumeric():
            if word not in unique_numbers:
                unique_numbers.append(word)
        else:
            word_lower = word.lower()
            if word_lower not in [w.lower() for w in unique_words]:
                unique_words.append(word)
            
            if word_lower in word_frequency:
                word_frequency[word_lower] += 1
            else:
                word_frequency[word_lower] = 1
    
    return unique_words, unique_numbers, word_frequency