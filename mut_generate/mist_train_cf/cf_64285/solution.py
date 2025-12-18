"""
QUESTION:
Create a function named `six_char_words` that takes a list of words as input and returns a list of words with exactly 6 characters.
"""

def six_char_words(words):
    """
    This function takes a list of words as input and returns a list of words with exactly 6 characters.
    
    Parameters:
    words (list): A list of words.
    
    Returns:
    list: A list of words with exactly 6 characters.
    """
    return [word for word in words if len(word) == 6]