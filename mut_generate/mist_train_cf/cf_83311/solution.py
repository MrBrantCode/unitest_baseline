"""
QUESTION:
Write a function `replace_punctuation_with_phrases` that takes a string `text` as input and returns the text with all punctuation marks replaced by their corresponding phrases in English. The function should respect the original position of the punctuation marks in the text. The punctuation marks and their corresponding phrases are: ! (exclamation mark), . (full stop), , (comma), ? (question mark), ; (semicolon), : (colon), - (hyphen), ' (apostrophe), " (double quotes), ( (left parenthesis), ) (right parenthesis), { (left curly brace), } (right curly brace), [ (left square bracket), ] (right square bracket), < (less than), > (greater than).
"""

def replace_punctuation_with_phrases(text):
    """
    Replaces punctuation marks in a given text with their corresponding phrases in English.

    Args:
    text (str): The input text.

    Returns:
    str: The text with all punctuation marks replaced by their corresponding phrases.
    """
    
    # Map each punctuation mark to its corresponding word
    punctuation_dict = {
        "!": " exclamation mark", 
        ".": " full stop", 
        ",": " comma",
        "?": " question mark",
        ";": " semicolon", 
        ":": " colon", 
        "-": " hyphen",
        "'": " apostrophe",
        '"': " double quotes",
        "(": " left parenthesis", 
        ")": " right parenthesis",
        "{": " left curly brace", 
        "}": " right curly brace",
        "[": " left square bracket", 
        "]": " right square bracket",
        "<": " less than", 
        ">": " greater than",
    }

    # Replace each punctuation mark in the text with its corresponding word
    for punctuation, phrase in punctuation_dict.items():
        text = text.replace(punctuation, phrase)

    return text