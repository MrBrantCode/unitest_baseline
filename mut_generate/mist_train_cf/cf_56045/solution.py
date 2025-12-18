"""
QUESTION:
Create a function named `reverse_order` that takes a string sentence as input and returns a string where the sequence of words is rearranged in reverse order, with any punctuation maintained at the end of the words they were originally attached to.
"""

def reverse_order(sentence):
    words = sentence.split(' ')
    reversed_words = [word[::-1] for word in reversed(words)]
    return ' '.join(word[::-1] for word in reversed_words)