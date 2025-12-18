"""
QUESTION:
Create a function `match_unique_words(sentence1: str, sentence2: str) -> bool` that checks if two provided sentences contain the same set of unique words in the same order. The function should return True if the sentences have the same unique words in the same order, and False otherwise. The comparison is case-sensitive.
"""

def match_unique_words(sentence1: str, sentence2: str) -> bool:
    """
    Check if two provided sentences contain the same set of unique words and in the same order.
    """
    # Split the sentences into list of words
    list_sentence1 = sentence1.split()
    list_sentence2 = sentence2.split()

    # Check if lists are same i.e., the words are in the same order and are unique
    return list_sentence1 == list_sentence2