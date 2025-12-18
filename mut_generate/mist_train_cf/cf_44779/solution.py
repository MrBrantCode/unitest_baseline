"""
QUESTION:
Create a function called `compare_word_sets` that takes two string parameters `phrase1` and `phrase2`. The function should return `True` if the sets of distinct terms (words) in `phrase1` and `phrase2` are identical, and `False` otherwise. The comparison should be case sensitive and consider word order irrelevant. The input phrases will only contain spaces as delimiters.
"""

def compare_word_sets(phrase1: str, phrase2: str):
    set1 = set(phrase1.split(' '))
    set2 = set(phrase2.split(' '))
    return set1 == set2