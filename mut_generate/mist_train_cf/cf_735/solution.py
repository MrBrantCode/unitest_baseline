"""
QUESTION:
Write a function called `reverse_words` that takes a sentence as input and returns a new sentence where each word is reversed, while maintaining the original order of the words.
"""

def reverse_words(sentence):
    words = sentence.split(" ")
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)