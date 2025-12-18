"""
QUESTION:
Write a function named `count_vowels` that takes a string `s` as input and returns the number of vowels in the string, ignoring any vowels that are followed by a consonant. The function should handle both uppercase and lowercase letters as vowels, treat special characters and numbers as non-vowel characters, and handle consecutive vowels and consonants accordingly. The function should also handle strings with no vowels and empty strings by returning 0.
"""

def count_vowels(s):
    """
    Returns the number of vowels in the string, ignoring any vowels that are followed by a consonant.

    Args:
        s (str): The input string.

    Returns:
        int: The number of vowels in the string.
    """
    vowels = 'aeiouAEIOU'
    count = 0
    prev_is_consonant = True
    for char in s:
        if char in vowels:
            if prev_is_consonant:
                count += 1
            prev_is_consonant = False
        elif char.isalpha():
            prev_is_consonant = True
        else:
            prev_is_consonant = True
    return count