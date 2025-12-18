"""
QUESTION:
Write a function named `most_common_sentence` that takes a list of distinct sentences as input and returns the sentence with the highest frequency of recurrence in the list. If multiple sentences have the same highest frequency, the function should return any of them. The input list contains unique sentences and each sentence is a string.
"""

from collections import Counter

def most_common_sentence(sentences):
    sentence_counter = Counter(sentences)
    return sentence_counter.most_common(1)[0][0]