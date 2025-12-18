"""
QUESTION:
Create a function named `char_frequency` that takes a string as input and returns a dictionary containing the frequencies of each non-vowel character in the string, ignoring case sensitivity. The function should only consider alphabetic characters and exclude vowels.
"""

def char_frequency(string):
    """
    Returns a dictionary containing the frequencies of each non-vowel character in the string, ignoring case sensitivity.

    Args:
        string (str): The input string.

    Returns:
        dict: A dictionary with non-vowel characters as keys and their frequencies as values.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    frequency_dict = {}

    for char in string.lower():
        if char not in vowels and char.isalpha():
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1

    return frequency_dict