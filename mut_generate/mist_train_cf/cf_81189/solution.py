"""
QUESTION:
Create a function named `extract_a_words` that takes a sentence as input and returns a list of words that start with the letter 'a', ignoring case. The function should split the sentence into individual words and consider only words that start with 'a' or 'A'.
"""

def extract_a_words(sentence):
    """
    This function takes a sentence as input and returns a list of words 
    that start with the letter 'a', ignoring case.
    
    Parameters:
    sentence (str): The input sentence.
    
    Returns:
    list: A list of words that start with the letter 'a'.
    """
    return [word for word in sentence.split() if word.lower().startswith('a')]