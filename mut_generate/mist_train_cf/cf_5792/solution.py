"""
QUESTION:
Write a function `tokenize_text(text)` that takes a string of text as input and returns a list of tokens. The function should handle multiple paragraphs, punctuation marks, special characters, nested parentheses, and quotation marks correctly. 

Each token can be a word, punctuation mark, or special character. The function should split the text into tokens based on these criteria. 

For example, the text "Hello, world!" should be tokenized into ["Hello", ",", "world", "!"]. Similarly, the text "(Hello, world!)" should be tokenized into ["(", "Hello", ",", "world", "!", ")"].
"""

import re

def tokenize_text(text):
    """
    Tokenize the given text into a list of tokens.

    Args:
    text (str): The input text to be tokenized.

    Returns:
    list: A list of tokens.
    """
    # Remove newline characters and replace with spaces
    text = re.sub('\n', ' ', text)

    # Tokenize the text
    tokens = re.findall(r'[\w\'\-]+|[.,!?;()"\']', text)

    return tokens