"""
QUESTION:
Create a function `compare_word_sets_frequency(phrase1: str, phrase2: str) -> bool` that determines whether two given phrases consist of identical sets of words with the same word frequency. The function should consider the frequency of each word in both phrases, returning `True` if the word frequencies match and `False` otherwise.
"""

def compare_word_sets_frequency(phrase1: str, phrase2: str) -> bool:
    """
    Determine whether the two input phrases consist of identical sets of words, with the same word frequency.
    For example, the word 'apple' appearing twice in the first phrase should also appear twice in the second phrase.
    """
    dict1 = {}
    dict2 = {}
    for word in phrase1.split():
        dict1[word] = dict1.get(word, 0) + 1
    for word in phrase2.split():
        dict2[word] = dict2.get(word, 0) + 1
    return dict1 == dict2