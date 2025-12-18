"""
QUESTION:
Write a function `reverse_sentence(sentence)` that takes a string of words as input and returns a string with the order of the words reversed, while maintaining the order of characters within each word. The input string may contain multiple words separated by a single space, and the output string should also use a single space to separate the words.
"""

def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)