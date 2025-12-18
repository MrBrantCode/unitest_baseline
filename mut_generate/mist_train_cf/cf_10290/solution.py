"""
QUESTION:
Create a function called `sentence_reverse` that takes a string containing a sentence as input and returns the sentence in reverse order. The sentence may contain special characters, punctuation, and multiple whitespaces.
"""

def sentence_reverse(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence