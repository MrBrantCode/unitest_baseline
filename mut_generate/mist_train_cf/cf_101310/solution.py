"""
QUESTION:
Write a function named `count_word_frequencies` that takes a string `text` as input and returns a dictionary where the keys are the words in the text and the values are their corresponding frequencies. The function should split the text into words based on whitespace characters and consider 'word' and 'Word' as the same word (case-insensitive). The function should also ignore punctuation marks.
"""

def count_word_frequencies(text):
    """
    This function takes a string `text` as input and returns a dictionary where the keys are the words in the text and the values are their corresponding frequencies.
    
    The function splits the text into words based on whitespace characters and considers 'word' and 'Word' as the same word (case-insensitive). It also ignores punctuation marks.

    Parameters:
    text (str): The input string.

    Returns:
    dict: A dictionary where the keys are the words in the text and the values are their corresponding frequencies.
    """
    import re
    from collections import Counter
    words = re.findall(r'\b\w+\b', text.lower())
    return dict(Counter(words))