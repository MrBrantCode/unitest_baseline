"""
QUESTION:
Find all words in a sentence that start with "th". The function should be case-insensitive. The function name should be find_th_words.
"""

def find_th_words(sentence):
    """
    Find all words in a sentence that start with 'th' in a case-insensitive manner.

    Args:
        sentence (str): The input sentence.

    Returns:
        list: A list of words that start with 'th'.
    """
    words = sentence.split()
    return [word for word in words if word.lower().startswith('th')]