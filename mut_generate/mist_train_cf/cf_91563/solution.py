"""
QUESTION:
Write a Python function named `reverse_sentence` that takes a sentence as input, reverses the order of the words, and keeps the order of characters within each word intact. The function should handle punctuation marks and multiple whitespaces between words appropriately.
"""

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence