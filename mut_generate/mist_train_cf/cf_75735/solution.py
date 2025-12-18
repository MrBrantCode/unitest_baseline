"""
QUESTION:
Create a function called `sort_words` that takes a list of words as input and returns a string containing the words in increasing alphabetical order, separated by commas. The input list will contain at least one word.
"""

def sort_words(word_list):
    """
    This function takes a list of words, sorts them in increasing alphabetical order, 
    and returns a string with the sorted words separated by commas.

    Parameters:
    word_list (list): A list of words.

    Returns:
    str: A string containing the words in increasing alphabetical order, separated by commas.
    """
    word_list.sort()
    return ', '.join(word_list)