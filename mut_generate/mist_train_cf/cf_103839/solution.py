"""
QUESTION:
Create a function named `count_vowels` that takes a string as input and returns the total number of vowels and their frequency. The function should consider both lowercase and uppercase vowels and count each occurrence. The vowels are 'a', 'e', 'i', 'o', and 'u'.
"""

def count_vowels(sentence):
    """
    This function takes a string as input and returns the total number of vowels and their frequency.

    Args:
        sentence (str): The input string.

    Returns:
        dict: A dictionary containing the total vowel count and the frequency of each vowel.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    vowel_frequency = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    for char in sentence:
        if char.lower() in vowels:
            vowel_count += 1
            vowel_frequency[char.lower()] += 1

    result = {
        'vowel_count': vowel_count,
        'vowel_frequency': vowel_frequency
    }
    return result