"""
QUESTION:
Create a function called word_counter that accepts a string as an argument. The function should return a dictionary containing all the unique words in the string as keys and the number of times each word occurs as values. The function should be case-insensitive and ignore punctuation. The function should also be able to handle non-English words. The input string may contain multiple sentences and words from different languages.
"""

import string

def word_counter(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.split()
    word_dict = {}
    for word in text:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    return word_dict