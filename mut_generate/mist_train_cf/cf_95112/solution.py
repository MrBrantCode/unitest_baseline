"""
QUESTION:
Create a function named `build_word_frequency_dict` that takes two parameters: `input_string` and `stop_words`. The function should return a dictionary where the keys are the words in `input_string` (ignoring punctuation, in lowercase, and excluding any words in `stop_words`) and the values are the corresponding word frequencies.
"""

import string

def build_word_frequency_dict(input_string, stop_words):
    """
    Returns a dictionary where the keys are the words in `input_string` 
    (ignoring punctuation, in lowercase, and excluding any words in `stop_words`) 
    and the values are the corresponding word frequencies.

    Parameters:
    input_string (str): The string from which to build the word frequency dictionary.
    stop_words (list): A list of words to be excluded from the dictionary.

    Returns:
    dict: A dictionary where the keys are the words in `input_string` and the values are the corresponding word frequencies.
    """

    # Remove punctuation marks
    input_string = input_string.translate(str.maketrans('', '', string.punctuation))

    # Convert all words to lowercase
    input_string = input_string.lower()

    # Remove stop words
    words = input_string.split()
    words = [word for word in words if word not in stop_words]

    # Initialize an empty dictionary
    word_freq_dict = {}

    # Iterate over each word and update the frequency in the dictionary
    for word in words:
        if word in word_freq_dict:
            word_freq_dict[word] += 1
        else:
            word_freq_dict[word] = 1

    # Return the final dictionary
    return word_freq_dict