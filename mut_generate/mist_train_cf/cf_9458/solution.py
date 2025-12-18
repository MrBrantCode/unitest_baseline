"""
QUESTION:
Create a function `word_count` that takes a string as input and returns a dictionary where the keys are the unique words in the string and the values are their corresponding frequencies. The function should be case-sensitive and consider punctuation as part of the word.
"""

def word_count(sentence):
    """
    Returns a dictionary with unique words in the sentence and their frequencies.
    
    The function is case-sensitive and considers punctuation as part of the word.
    
    Parameters:
    sentence (str): Input string.
    
    Returns:
    dict: Dictionary with words as keys and their frequencies as values.
    """
    return {word: sentence.split().count(word) for word in set(sentence.split())}