"""
QUESTION:
Write a function `reverse_words` that takes a list of words as input, where each word is a string, and returns a new list where each word has its characters reversed. The input list is guaranteed to be non-empty.
"""

def reverse_words(words):
    """
    This function takes a list of words, reverses each word, and returns the new list.
    
    Args:
        words (list): A list of strings where each string is a word.
    
    Returns:
        list: A list of strings where each string is a reversed word from the input list.
    """
    return [word[::-1] for word in words]