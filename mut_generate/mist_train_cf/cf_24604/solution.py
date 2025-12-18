"""
QUESTION:
Create a function called `sort_strings_alphabetically` that takes a list of strings as input. The function must return a string containing all the input strings, sorted in alphabetical order and separated by spaces.
"""

def sort_strings_alphabetically(words):
    """
    This function takes a list of strings, sorts them alphabetically, and returns a string containing all the input strings, separated by spaces.

    Parameters:
    words (list): A list of strings

    Returns:
    str: A string containing all the input strings, sorted in alphabetical order and separated by spaces
    """
    # Use the built-in sorted() function to sort the list of strings
    sorted_words = sorted(words)
    # Join the sorted list of words separated by spaces
    return " ".join(sorted_words)