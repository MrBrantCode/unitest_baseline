"""
QUESTION:
Write a function named 'process_word_list' that takes a list of strings as input. The function should convert the input list to lowercase, remove any duplicate words, and sort the words in alphabetical order. The function should return the processed list.
"""

def process_word_list(word_list):
    """
    This function processes a list of strings by converting it to lowercase, 
    removing any duplicate words, and sorting the words in alphabetical order.

    Args:
        word_list (list): A list of strings.

    Returns:
        list: The processed list of words.
    """
    return sorted(set(word.lower() for word in word_list))