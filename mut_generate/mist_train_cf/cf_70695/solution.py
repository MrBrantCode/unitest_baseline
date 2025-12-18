"""
QUESTION:
Write a function named `count_vowels` that takes a string `s` as input and returns a dictionary where the keys are the vowels found in the string and the values are their respective occurrence counts. The function should be case-insensitive, treating both lowercase and uppercase vowels as the same character.
"""

def count_vowels(s):
    """
    This function takes a string `s` as input and returns a dictionary where the keys are the vowels found in the string 
    and the values are their respective occurrence counts. The function is case-insensitive.

    Args:
        s (str): The input string.

    Returns:
        dict: A dictionary with vowels as keys and their counts as values.
    """

    # Define the set of vowels, including both lower-case and upper-case.
    vowels = set('aeiouAEIOU')

    # Create a dictionary to store the vowel count.
    vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Go through each character in the string.
    for char in s:
        # If the character is a vowel, increment the count in the dictionary.
        if char in vowels:
            vowel_count[char.lower()] += 1

    # Filter out the vowels that didn't occur in the string.
    vowel_count = {vowel: count for vowel, count in vowel_count.items() if count > 0}

    return vowel_count