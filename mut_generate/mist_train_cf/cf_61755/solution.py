"""
QUESTION:
Write a function `calculate_word_frequency` that takes two sentences as input and returns a dictionary with unique words as keys and their frequencies as values. The comparison should be case-insensitive and the words should be separated by spaces. The function should combine the word frequencies from both sentences.
"""

from collections import Counter

def calculate_word_frequency(sentence1, sentence2):
    """
    Calculate the frequency of each word in two sentences.

    Args:
    sentence1 (str): The first sentence.
    sentence2 (str): The second sentence.

    Returns:
    dict: A dictionary with unique words as keys and their frequencies as values.
    """
    # Convert sentences to lower case and split into word lists
    word_list1 = sentence1.lower().split()
    word_list2 = sentence2.lower().split()

    # Create dictionaries of word frequencies for each sentence
    counter1 = Counter(word_list1)
    counter2 = Counter(word_list2)

    # Combine the two dictionaries
    combined_counter = counter1 + counter2

    return dict(combined_counter)