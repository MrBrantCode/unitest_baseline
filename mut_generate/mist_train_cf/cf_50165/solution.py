"""
QUESTION:
Write a function `count_uncommon_punctuation(sentence)` that takes a string `sentence` as input and returns a dictionary-like object where each key-value pair corresponds to an uncommon punctuation mark and its count in the sentence. The function should consider a set of common punctuation marks ({'.', ',', '!', '?', ';', ':', "'", '"'}), and count the occurrences of each punctuation mark that is not in this set and is classified as punctuation by its Unicode category. The function should work efficiently for large inputs and handle Unicode sentences.
"""

from collections import Counter
import unicodedata

def count_uncommon_punctuation(sentence):
    common_punctuation = {'.', ',', '!', '?', ';', ':', "'", '"'}
    uncommon_punctuation = [char for char in sentence if unicodedata.category(char).startswith('P') and char not in common_punctuation]
    return Counter(uncommon_punctuation)