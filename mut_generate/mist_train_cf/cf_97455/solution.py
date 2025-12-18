"""
QUESTION:
Implement a class with a method `process_string` that takes a string as input, and a method `get_max_frequency_word` that returns the word with the maximum frequency in the input string. The `process_string` method should ignore punctuation marks and consider only alphabetic characters in the string. If multiple words have the same maximum frequency, the method should return the word that occurs first in the string. The class should be able to handle large input strings efficiently.
"""

import string
from collections import defaultdict

def entance(input_string):
    """
    This function takes a string as input, ignores punctuation marks, 
    and returns the word with the maximum frequency in the string. 
    If multiple words have the same maximum frequency, it returns 
    the word that occurs first in the string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The word with the maximum frequency in the input string.
    """
    # Convert the string to lower case and remove punctuation marks
    input_string = input_string.lower()
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))

    # Split the string into words
    words = input_string.split()

    # Create a dictionary to store the frequency of each word
    freq_dict = defaultdict(int)

    # Initialize variables to store the maximum frequency and the corresponding word
    max_freq = 0
    max_word = None

    # Iterate over each word in the string
    for word in words:
        # Increment the frequency of the word
        freq_dict[word] += 1

        # Update the maximum frequency and the corresponding word if necessary
        if freq_dict[word] > max_freq:
            max_freq = freq_dict[word]
            max_word = word

    # Return the word with the maximum frequency
    return max_word