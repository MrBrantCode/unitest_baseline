"""
QUESTION:
Write a function `reverse_sentence(sentence)` that takes a sentence as input and returns the sentence with the order of the words reversed, while keeping the order of the characters within each word intact. The function should handle punctuation marks and multiple whitespaces between words appropriately.
"""

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence