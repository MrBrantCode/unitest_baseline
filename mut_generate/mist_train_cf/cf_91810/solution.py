"""
QUESTION:
Write a function named `count_unique_words` that takes a string `text` as input and returns the number of unique words in the text. The function should disregard punctuation marks and consider words in a case-insensitive manner. It should also remove any leading or trailing whitespaces from each word before considering it as a unique word.
"""

import string

def count_unique_words(text):
    # Remove punctuation marks from the text
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Split the text into words and convert them to lowercase
    words = text.lower().split()

    # Create a dictionary to store unique words and their counts
    unique_words = {}

    # Iterate over each word and update the counts in the dictionary
    for word in words:
        word = word.strip()
        if word not in unique_words:
            unique_words[word] = 1
        else:
            unique_words[word] += 1

    # Return the number of unique words
    return len(unique_words)