"""
QUESTION:
Create a function called `reverse_sentence` that takes a string of words as input and returns the string with the words in reverse order.
"""

def reverse_sentence(sentence):
    words = sentence.split(' ')
    reverse_words = words[::-1]
    reverse_sentence = ' '.join(reverse_words)
    return reverse_sentence