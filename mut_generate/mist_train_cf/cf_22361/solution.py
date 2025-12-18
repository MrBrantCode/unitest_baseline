"""
QUESTION:
Write a function `calculate_letter_frequency` that takes a string `word` as input and returns a dictionary where the keys are the unique letters in the word and the values are their corresponding frequencies. The function should have a time complexity of O(n), where n is the length of the word, and a space complexity of O(1), where the size of the dictionary is limited to the number of unique letters in the word.
"""

def calculate_letter_frequency(word):
    """
    Calculate the frequency of each unique letter in a given word.

    Args:
        word (str): The input word.

    Returns:
        dict: A dictionary where the keys are the unique letters in the word and the values are their corresponding frequencies.
    """
    frequency = {}
    for char in word:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency