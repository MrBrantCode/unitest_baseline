"""
QUESTION:
Create a function `reverse_sentence(sentence)` that takes a string sentence as input, reverses the order of words in the sentence, and returns the resulting string without reversing individual words or modifying special characters and spaces.
"""

def reverse_sentence(sentence):
    words = sentence.split(" ")
    reversed_words = words[::-1]
    reversed_sentence = " ".join(reversed_words)
    return reversed_sentence