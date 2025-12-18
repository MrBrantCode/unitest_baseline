"""
QUESTION:
Write a function named `modify_sentence` that takes a sentence as input and returns the modified sentence. The function should convert all the letters in the sentence to lowercase and exclude any punctuation marks or special characters from the output. The modified sentence should include spaces between words.
"""

def modify_sentence(sentence):
    """
    This function takes a sentence as input, converts it to lowercase, 
    excludes punctuation marks or special characters, and returns the modified sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        str: The modified sentence.
    """
    lowercase_sentence = sentence.lower()
    modified_sentence = ""
    for char in lowercase_sentence:
        if char.isalpha() or char.isspace():
            modified_sentence += char
    return modified_sentence