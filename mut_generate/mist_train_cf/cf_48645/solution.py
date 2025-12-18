"""
QUESTION:
Create a function `long_words_dict` that takes a list of words as input and returns a dictionary containing only the words with more than 7 characters, with their lengths as the values. Use the `map` function and a lambda function to achieve this.
"""

def long_words_dict(words):
    """
    Returns a dictionary containing words with more than 7 characters and their lengths.

    Args:
        words (list): A list of words.

    Returns:
        dict: A dictionary with words as keys and their lengths as values.
    """
    result = dict(map(lambda word: (word, len(word)) if len(word) > 7 else (None, None), words))
    return {k: v for k, v in result.items() if k is not None}