"""
QUESTION:
Write a function `longest_word_without_duplicates` that takes a sentence as input and returns the longest word without any duplicate letters. If there are multiple words with the same maximum length without duplicates, it can return any of them.
"""

def longest_word_without_duplicates(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Initialize variables to store the longest word and its length
    longest_word = ''
    longest_length = 0

    # Iterate over each word in the sentence
    for word in words:
        # Check if the word contains duplicate letters
        if len(set(word)) == len(word):
            # Check if the length of the current word is greater than the longest word found so far
            if len(word) > longest_length:
                longest_word = word
                longest_length = len(word)

    return longest_word