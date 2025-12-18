"""
QUESTION:
Write a function `char_frequency` that takes a string `sentence` as input and returns a dictionary where each unique character in the sentence is a key and the frequency of each character is the corresponding value. The function should include all characters, including spaces and punctuation.
"""

def char_frequency(sentence):
    """
    Returns a dictionary with unique characters in the sentence as keys and their frequencies as values.

    Args:
    sentence (str): The input string.

    Returns:
    dict: A dictionary where each key is a unique character and its corresponding value is the frequency.
    """
    char_frequency = {}
    for char in sentence:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1
    return char_frequency