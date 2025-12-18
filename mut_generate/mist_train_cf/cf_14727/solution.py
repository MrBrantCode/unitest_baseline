"""
QUESTION:
Create a function named `check_valid_words` that takes a list of strings as input and returns True if all the strings are valid English words, and False otherwise. The function should ignore duplicate words in the input list and only count each word once. It has access to a set of all valid English words.
"""

def check_valid_words(word_list, valid_words):
    """
    Checks if all unique words in the input list are valid English words.
    
    Args:
        word_list (list): A list of strings to be checked.
        valid_words (set): A set of all valid English words.
    
    Returns:
        bool: True if all unique words are valid, False otherwise.
    """
    unique_words = set(word_list)
    
    for word in unique_words:
        if word not in valid_words:
            return False
    
    return True