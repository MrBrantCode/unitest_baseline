"""
QUESTION:
Replace a word with its synonym in a sentence. The function should take a sentence and a dictionary of word-synonym pairs as input, and return the modified sentence with all occurrences of the word replaced by its synonym. Use Python's built-in `re` module and consider the word's grammatical forms (e.g., singular and plural forms).
"""

import re
def replace_with_synonym(sentence, synonyms):
    """
    Replace a word with its synonym in a sentence.
    
    Args:
    sentence (str): The input sentence.
    synonyms (dict): A dictionary of word-synonym pairs.
    
    Returns:
    str: The modified sentence with all occurrences of the word replaced by its synonym.
    """
    pattern = re.compile(r'\b(' + '|'.join(synonyms.keys()) + r')\b')
    return pattern.sub(lambda x: synonyms[x.group()], sentence)