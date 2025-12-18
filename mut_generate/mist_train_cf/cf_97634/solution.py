"""
QUESTION:
Write a function called `sort_words` that sorts a given list of words in alphabetical order, ignoring the original case. The function should take a list of strings as input and return a string where the sorted words are joined together with a space in between.
"""

def sort_words(word_list):
    """
    Sorts a given list of words in alphabetical order, ignoring the original case.
    
    Args:
        word_list (list): A list of strings.
    
    Returns:
        str: A string where the sorted words are joined together with a space in between.
    """
    return ' '.join(sorted(word_list, key=str.lower))