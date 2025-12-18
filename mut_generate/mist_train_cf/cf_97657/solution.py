"""
QUESTION:
Write a function `replace_word_with_synonym(sentence, word, synonyms)` that replaces all occurrences of a specific word in a sentence with its corresponding synonym. The function should take a sentence, the word to be replaced, and a dictionary of synonyms as input. The function should use the `re` module and return the modified sentence. The dictionary of synonyms should contain different forms of the word (e.g., singular, plural, past tense, etc.).
"""

import re

def replace_word_with_synonym(sentence, word, synonyms):
    """
    Replaces all occurrences of a specific word in a sentence with its corresponding synonym.

    Args:
        sentence (str): The input sentence.
        word (str): The word to be replaced.
        synonyms (dict): A dictionary of synonyms for the word.

    Returns:
        str: The modified sentence.
    """
    pattern = re.compile(r'\b(' + '|'.join(synonyms.keys()) + r')\b')
    modified_sentence = pattern.sub(lambda x: synonyms[x.group()], sentence)
    return modified_sentence