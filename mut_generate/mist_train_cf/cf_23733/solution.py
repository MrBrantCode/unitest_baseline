"""
QUESTION:
Write a function called `reverse_words` that takes an English sentence as input and returns the sentence with its words in reverse order. The function should not change the order of characters within each word, but only reverse the order of the words themselves.
"""

def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words)