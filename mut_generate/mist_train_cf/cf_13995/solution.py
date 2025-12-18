"""
QUESTION:
Create a function named `sort_word_lengths` that takes a string of comma-separated words as input and returns a list of tuples, where each tuple contains a word and its length. The list should be sorted in descending order based on the word lengths.
"""

def sort_word_lengths(input_str):
    """
    This function takes a string of comma-separated words, 
    and returns a list of tuples containing each word and its length, 
    sorted in descending order based on the word lengths.

    Args:
        input_str (str): A string of comma-separated words.

    Returns:
        list: A list of tuples, where each tuple contains a word and its length.
    """
    word_list = input_str.split(", ")
    return sorted([(word, len(word)) for word in word_list], key=lambda x: x[1], reverse=True)