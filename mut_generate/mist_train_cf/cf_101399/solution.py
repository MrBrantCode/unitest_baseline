"""
QUESTION:
Create a function called `sort_adjectives_adverbs` that takes a list of words as input and returns two separate lists, one for adjectives and one for adverbs. The function should classify a word as an adverb if it ends with the suffix "ly", otherwise, it should be classified as an adjective.
"""

def sort_adjectives_adverbs(words):
    """
    This function takes a list of words and returns two separate lists, 
    one for adjectives and one for adverbs. A word is classified as an 
    adverb if it ends with the suffix "ly", otherwise, it is classified 
    as an adjective.

    Args:
    words (list): A list of words

    Returns:
    tuple: Two lists, the first for adjectives and the second for adverbs
    """
    adjectives = [word for word in words if not word.endswith("ly")]
    adverbs = [word for word in words if word.endswith("ly")]
    return adjectives, adverbs