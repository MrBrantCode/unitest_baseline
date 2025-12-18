"""
QUESTION:
Create a function `word_frequency` that takes a string `text` as input and returns a dictionary where the keys are the unique words in the text and the values are their corresponding frequencies. The function should be case-insensitive (i.e., it should treat 'The' and 'the' as the same word). Assume that words are separated by spaces and that punctuation is part of the word (e.g., 'dog.' and 'dog' are treated as different words).
"""

def word_frequency(text):
    # Convert text to lowercase and split it into words
    words = text.lower().split()

    # Count the frequency of each word
    word_count = {}
    for word in words:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

    return word_count