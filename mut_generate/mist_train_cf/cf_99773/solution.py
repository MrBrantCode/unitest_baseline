"""
QUESTION:
Write a function called `reverse_sentence` that takes a sentence as input, reverses the order of its words, and returns the resulting sentence with the first letter capitalized and ending with a period.
"""

def entance(sentence):
    words = sentence.split()
    words.reverse()
    return ' '.join(words).capitalize() + '.'