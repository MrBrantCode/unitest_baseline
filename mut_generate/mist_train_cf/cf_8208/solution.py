"""
QUESTION:
Create a function called `process_word_list` that takes a list of words as input, makes the list case-insensitive, removes duplicates, sorts the words in alphabetical order, and then reverses the sorted list. The function should return the processed list.
"""

def process_word_list(word_list):
    """
    Process a list of words by making it case-insensitive, removing duplicates, 
    sorting in alphabetical order, and reversing the sorted list.

    Args:
        word_list (list): The list of words to be processed.

    Returns:
        list: The processed list of words.
    """
    word_list = [word.lower() for word in word_list]  # Convert all words to lowercase
    word_list = list(set(word_list))  # Remove duplicate words
    word_list.sort()  # Sort the words in alphabetical order
    return word_list[::-1]  # Reverse the order of the sorted words