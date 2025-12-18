"""
QUESTION:
Write a function `vowel_indices` that takes a string of lowercase letters and spaces as input and returns the total count of vowels and their indices in the string. The string does not contain uppercase letters, punctuation, or special characters.
"""

def vowel_indices(word):
    """
    This function calculates the total count of vowels and their indices in a given string.

    Args:
    word (str): A string of lowercase letters and spaces.

    Returns:
    tuple: A tuple containing the total count of vowels and their indices in the string.
    """
    vowels = 'aeiou'
    count = 0
    indices = []
    for i, char in enumerate(word):
        if char in vowels:
            count += 1
            indices.append(i + 1)  # Add 1 to the index for 1-based indexing
    return count, indices