"""
QUESTION:
Implement a function `reverse_capitalize(sentence)` that takes a string sentence as input, capitalizes each word in the sentence, and reverses the order of the words. The function should handle special characters and white spaces accordingly.
"""

def reverse_capitalize(sentence):
    words = [word.capitalize() for word in sentence.split()]
    return ' '.join(words[::-1])