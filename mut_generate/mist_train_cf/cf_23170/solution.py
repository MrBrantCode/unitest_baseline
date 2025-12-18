"""
QUESTION:
Write a function `process_string` that takes a string as input, processes it to find the word with the maximum frequency, and returns this word. The function should ignore punctuation marks, consider only alphabetic characters, and be case-insensitive. In case of multiple words with the same maximum frequency, the function should return the word that occurs first in the string. The function should be efficient enough to handle large input strings.
"""

import string
from collections import defaultdict

def process_string(input_string):
    """
    This function processes the input string to find the word with the maximum frequency.
    It ignores punctuation marks, considers only alphabetic characters, and is case-insensitive.
    In case of multiple words with the same maximum frequency, it returns the word that occurs first in the string.

    Args:
        input_string (str): The input string to be processed.

    Returns:
        str: The word with the maximum frequency in the input string.
    """

    # Convert the input string to lower case and remove punctuation marks
    input_string = input_string.lower()
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))

    # Split the input string into words
    words = input_string.split()

    # Create a dictionary to store the frequency of each word
    freq_dict = defaultdict(int)

    # Initialize variables to store the maximum frequency and the corresponding word
    max_freq = 0
    max_word = None

    # Iterate over the words in the input string
    for word in words:
        # Increment the frequency of the current word
        freq_dict[word] += 1

        # Update the maximum frequency and the corresponding word if necessary
        if freq_dict[word] > max_freq:
            max_freq = freq_dict[word]
            max_word = word

    # Return the word with the maximum frequency
    return max_word