"""
QUESTION:
Create a function `match_unique_words(sentence1: str, sentence2: str) -> bool` that takes two sentences as input and returns a boolean value indicating whether the sentences contain the same unique words in the same order, ignoring duplicates and word frequency.
"""

def match_unique_words(sentence1: str, sentence2: str) -> bool:
    """
    Confirm whether the contents and order of unique words in two provided sentences match.
    """
    words1 = list(dict.fromkeys(sentence1.split()))
    words2 = list(dict.fromkeys(sentence2.split()))

    return words1 == words2