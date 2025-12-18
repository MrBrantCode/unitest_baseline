"""
QUESTION:
Create a function named `sort_words_by_length` that takes a list of words as input and returns a JSON string. The JSON string should be a list of dictionaries, each containing a word and its length, sorted in ascending order by the word length.
"""

import json

def sort_words_by_length(words):
    """
    This function takes a list of words, sorts them in ascending order by their lengths,
    and returns a JSON string containing a list of dictionaries with the word and its length.

    Args:
        words (list): A list of words

    Returns:
        str: A JSON string containing a list of dictionaries
    """
    # Sort the words based on their length
    sorted_words = sorted(words, key=len)
    
    # Create a list of dictionaries containing the word and its length
    word_list = [{"word": word, "length": len(word)} for word in sorted_words]
    
    # Convert the list to JSON format
    return json.dumps(word_list)