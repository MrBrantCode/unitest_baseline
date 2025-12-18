"""
QUESTION:
Create a function named `filter_lexemes` that utilizes list comprehension to filter a list of input words (`input_list`) based on two conditions: the word must be longer than 5 characters, and the word must be present in a given comprehensive lexicon (`lexicon`). Return the filtered list of words.
"""

def filter_lexemes(input_list, lexicon):
    """
    Filters a list of input words based on two conditions:
    1. The word must be longer than 5 characters.
    2. The word must be present in a given comprehensive lexicon.
    
    Args:
        input_list (list): List of input words to be filtered.
        lexicon (list): Comprehensive list of valid words.
    
    Returns:
        list: Filtered list of words.
    """
    return [word for word in input_list if len(word) > 5 and word in lexicon]