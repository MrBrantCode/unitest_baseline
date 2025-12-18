"""
QUESTION:
Create a function named `compare_sentences` that takes two string parameters and returns a dictionary containing characters that appear in identical positions in both strings, regardless of case, along with their respective counts. The function should ignore case differences and consider all characters including spaces and punctuation.
"""

from collections import defaultdict

def compare_sentences(sentence1, sentence2):
    result = defaultdict(int)
    for ch1, ch2 in zip(sentence1.lower(), sentence2.lower()):
        if ch1 == ch2:
            result[ch1] += 1
    return dict(result)