"""
QUESTION:
Write a function named `count_synonyms` that takes a dictionary `lexicon` where each key is a word and its corresponding value is a list of its synonyms. The function should return a dictionary where each key is a word from the `lexicon` and its corresponding value is the number of its synonyms.
"""

def count_synonyms(lexicon):
    """
    This function takes a dictionary of words and their synonyms, and returns a dictionary with each word and its synonym count.

    Args:
        lexicon (dict): A dictionary where each key is a word and its corresponding value is a list of its synonyms.

    Returns:
        dict: A dictionary where each key is a word from the lexicon and its corresponding value is the number of its synonyms.
    """
    synonym_counts = {}

    for key, synonyms in lexicon.items():
        synonym_counts[key] = len(synonyms)

    return synonym_counts