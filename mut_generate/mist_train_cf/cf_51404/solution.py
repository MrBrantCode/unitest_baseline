"""
QUESTION:
Create a function named `reverse_word_frequencies` that takes a string as input and returns a dictionary where the keys are the reversed words from the string with more than 4 characters and the values are their frequencies. The function should not take any other parameters and should not modify the input string.
"""

from collections import Counter

def reverse_word_frequencies(input_string):
    """
    Returns a dictionary where the keys are the reversed words from the string 
    with more than 4 characters and the values are their frequencies.

    Parameters:
    input_string (str): The input string.

    Returns:
    dict: A dictionary where the keys are the reversed words and the values are their frequencies.
    """

    # Split the string into words
    words = input_string.split()

    # Filter out words that exceed 4 characters and reverse them
    reversed_words = [word[::-1] for word in words if len(word) > 4]

    # Count the frequency of each reversed word
    frequency = Counter(reversed_words)

    return dict(frequency)