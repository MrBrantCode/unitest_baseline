"""
QUESTION:
Write a function `count_vowels` that takes a string as input and returns the total count of vowels in the string and their indices. The input string contains only letters (both lowercase and uppercase), spaces, and punctuation marks. The function should be case-insensitive when counting vowels.
"""

def count_vowels(input_string):
    """
    Counts the total number of vowels in a given string and their indices.

    Args:
    input_string (str): The input string containing letters, spaces, and punctuation marks.

    Returns:
    tuple: A tuple containing the total count of vowels and their indices.
    """
    vowels = 'aeiouAEIOU'
    vowel_indices = []
    count = 0

    for index, char in enumerate(input_string):
        if char in vowels:
            vowel_indices.append((char, index))
            count += 1

    return count, vowel_indices