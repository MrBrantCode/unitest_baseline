"""
QUESTION:
Create a function called `find_words_ending_with_s` that takes a string as input and returns a list of words that end with the letter 's'. The function should consider words that end with 's' before punctuation as well. For example, the word "seashore." should be included in the output. The input string can contain any number of words, and each word can be followed by any punctuation mark.
"""

import string

def find_words_ending_with_s(text):
    # Split the text into words
    words = text.split()

    # Create an empty list to store the words that end with 's'
    end_s = []

    # Loop through each word in the word list
    for word in words:
        # Remove punctuation from the word and check if it ends with 's'
        if word.strip(string.punctuation).lower().endswith('s'):
            end_s.append(word)

    return end_s