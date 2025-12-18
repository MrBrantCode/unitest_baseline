"""
QUESTION:
Write a function named `verify_same_word_sets_freqs` that takes two string parameters `phrase1` and `phrase2`. The function should return `True` if the two phrases contain exactly the same set of words with the same frequency, and `False` otherwise. The comparison should be case-insensitive, meaning 'Apple' and 'apple' are considered the same word.
"""

def verify_same_word_sets_freqs(phrase1: str, phrase2: str) -> bool:
    word_dict1 = {word: phrase1.lower().split().count(word) for word in phrase1.lower().split()}
    word_dict2 = {word: phrase2.lower().split().count(word) for word in phrase2.lower().split()}
    return word_dict1 == word_dict2