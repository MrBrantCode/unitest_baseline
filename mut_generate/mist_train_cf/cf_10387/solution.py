"""
QUESTION:
Create a function called `find_word_occurrences` that takes a string `text` as input and returns the number of occurrences of the word "the" (case insensitive) in the text, excluding occurrences where "the" is part of another word or substring.
"""

def find_word_occurrences(text):
    """
    Returns the number of occurrences of the word "the" (case insensitive) in the text,
    excluding occurrences where "the" is part of another word or substring.
    
    Parameters:
    text (str): The input text to search for the word "the".
    
    Returns:
    int: The number of occurrences of the word "the" in the text.
    """
    words = text.lower().split()
    return words.count("the")