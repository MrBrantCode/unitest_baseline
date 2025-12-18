"""
QUESTION:
Write a function named `match_unique_words` that takes two string parameters, `sentence1` and `sentence2`, and returns a boolean indicating whether they contain the same collection of unique words, disregarding order and duplicates. The function should consider only spaces as word delimiters.
"""

def match_unique_words(sentence1: str, sentence2: str) -> bool:
    words1 = set(sentence1.split())
    words2 = set(sentence2.split())
    return words1 == words2