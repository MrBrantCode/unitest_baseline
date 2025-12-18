"""
QUESTION:
Write a function `character_frequency(sentence)` that calculates the frequency of each unique character in a given sentence, ignoring blank spaces, punctuation, and case differences. The function should then return the three most frequent characters along with their frequencies. The input sentence can be a long string, such as a paragraph or a short story.
"""

import collections
import string

def character_frequency(sentence):
    cleaned_sentence = sentence.replace(' ', '').lower()
    table = str.maketrans('', '', string.punctuation)
    cleaned_sentence = cleaned_sentence.translate(table)
    frequency = collections.Counter(cleaned_sentence)
    top_three_characters = frequency.most_common(3)
    return top_three_characters