"""
QUESTION:
Write a function called `alphabetical_sentence` that takes a sentence as input, splits it into words, and returns the words in alphabetical order, regardless of their original case in the sentence.
"""

def alphabetical_sentence(sentence):
    word_list = sentence.lower().split()
    word_list.sort()
    return ' '.join(word_list)