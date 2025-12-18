"""
QUESTION:
Write a function named `longest_words` that takes a string of words as input, finds all the words with the longest length, and returns them in reverse order of appearance. The function should handle cases where there are multiple words with the same longest length. The input string will only contain spaces as word delimiters and will not be empty.
"""

def longest_words(input_string):
    """
    Finds all the words with the longest length in a given string and returns them in reverse order of appearance.

    Args:
        input_string (str): A string of words.

    Returns:
        list: A list of words with the longest length in reverse order of appearance.
    """
    words = input_string.split()
    longest_length = 0
    longest_words = []

    for word in words:
        if len(word) > longest_length:
            longest_length = len(word)
            longest_words = [word]
        elif len(word) == longest_length:
            longest_words.append(word)

    longest_words.reverse()
    return longest_words