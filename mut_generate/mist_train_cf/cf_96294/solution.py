"""
QUESTION:
Write a function `get_top_ten_words` that takes a string of up to 100,000 characters as input, where words have a maximum length of 50 characters, and returns the top ten most used words excluding any words that contain numbers or special characters. The function should run in O(n log n) time complexity, where n is the number of words in the string.
"""

import re

def get_top_ten_words(input_string):
    """
    Returns the top ten most used words in the input string, excluding any words that contain numbers or special characters.

    Args:
        input_string (str): The input string.

    Returns:
        list: A list of the top ten most used words.
    """

    # Split the string into individual words
    words = input_string.split()

    # Create a dictionary to store the frequency of each word
    word_freq = {}

    # Iterate over each word and update its frequency in the dictionary if it does not contain numbers or special characters
    for word in words:
        if not re.search('[^a-zA-Z]', word):
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1

    # Sort the dictionary by values in descending order to get the most used words
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)

    # Extract the top ten most used words from the sorted list
    top_ten_words = [word[0] for word in sorted_words[:10]]

    return top_ten_words