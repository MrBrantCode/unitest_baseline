"""
QUESTION:
Create a function `process_string` that takes an input string and returns the following:
- The input string converted to lowercase with all non-alphanumeric characters removed.
- The number of vowels in the resulting string.
- The number of consonants in the resulting string.
- A dictionary with the frequency of each vowel in the resulting string.
- A dictionary with the frequency of each consonant in the resulting string.
The function should consider 'a', 'e', 'i', 'o', 'u' as vowels and all other alphanumeric characters as consonants.
"""

def process_string(input_string):
    """
    This function processes an input string, converting it to lowercase and removing non-alphanumeric characters.
    It then returns the processed string, the number of vowels and consonants, and their respective frequency dictionaries.

    Parameters:
    input_string (str): The input string to be processed.

    Returns:
    tuple: A tuple containing the processed string, number of vowels, number of consonants, vowel frequency dictionary, and consonant frequency dictionary.
    """

    # Convert string to lowercase and remove special characters
    processed_string = ''.join(e for e in input_string.lower() if e.isalnum())

    # Initialize counters for vowels and consonants
    vowels = 0
    consonants = 0

    # Initialize frequency dictionaries for vowels and consonants
    vowel_freq = {}
    consonant_freq = {}

    # Iterate through each character in the string
    for char in processed_string:
        if char in "aeiou":
            # Increment vowel count
            vowels += 1
            # Update vowel frequency dictionary
            vowel_freq[char] = vowel_freq.get(char, 0) + 1
        else:
            # Increment consonant count
            consonants += 1
            # Update consonant frequency dictionary
            consonant_freq[char] = consonant_freq.get(char, 0) + 1

    # Return the results
    return (processed_string, vowels, consonants, vowel_freq, consonant_freq)