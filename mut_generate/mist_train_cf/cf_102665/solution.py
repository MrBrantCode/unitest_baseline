"""
QUESTION:
Write a function `longest_word_unique_letters` that takes a sentence as input and returns the number of unique letters in the longest word of the sentence.
"""

def longest_word_unique_letters(sentence):
    words = sentence.split()
    max_unique = 0
    for word in words:
        unique_letters = len(set(word))
        max_unique = max(max_unique, unique_letters)
    return max_unique