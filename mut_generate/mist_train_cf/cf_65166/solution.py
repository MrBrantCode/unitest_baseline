"""
QUESTION:
Create a function `compare_word_sets` that takes two strings `phrase1` and `phrase2`, and a boolean `order`, as input. The function should return `True` if the two input strings contain the same unique words, considering case sensitivity and punctuation, and `False` otherwise. If `order` is `True`, the function should also consider the order of the words.
"""

def compare_word_sets(phrase1: str, phrase2: str, order: bool):
    """
    Analyze if two sentences contain precisely the identical unique words factoring in case sensitivity, punctuation and maintaining word order.
    """
    # Split sentences into words, retaining punctuation
    words1 = phrase1.split()
    words2 = phrase2.split()
    
    # If order matters
    if order:
        # Compare word lists directly
        return words1 == words2
    else:
        # Compare sorted word lists
        return sorted(words1) == sorted(words2)