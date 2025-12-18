"""
QUESTION:
Create a function called `tokenize_sentence` that tokenizes a given sentence using regular expressions. The function should only include words that start with a capital letter and have a length of at least 4 characters, and remove any punctuation marks before tokenizing.
"""

import re

def tokenize_sentence(sentence):
    """
    Tokenize a given sentence using regular expressions.
    
    The function only includes words that start with a capital letter and have a length of at least 4 characters, 
    and removes any punctuation marks before tokenizing.

    Args:
        sentence (str): The input sentence to be tokenized.

    Returns:
        list: A list of tokenized words.
    """
    # Remove punctuation marks from the sentence
    sentence_no_punct = re.sub(r'[^\w\s]', '', sentence)
    
    # Split the sentence into words
    words = sentence_no_punct.split()
    
    # Filter words that start with a capital letter and have a length of at least 4 characters
    tokenized_words = [word for word in words if word[0].isupper() and len(word) >= 4]
    
    return tokenized_words