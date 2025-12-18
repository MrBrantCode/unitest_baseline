"""
QUESTION:
Create a function `find_closest_vowel_subsequence(word)` that takes an English word as input and returns the nearest vowel situated between two consonants from the right side of the word, ignoring vowels at the beginning or end of the word. If no such vowel is found, return an empty string. The input string contains only English letters.
"""

def find_closest_vowel_subsequence(word):
    """
    This function takes an English word as input and returns the nearest vowel 
    situated between two consonants from the right side of the word, ignoring 
    vowels at the beginning or end of the word. If no such vowel is found, 
    return an empty string.

    Args:
        word (str): The input English word.

    Returns:
        str: The nearest vowel between two consonants.
    """
    vowels = 'aeiouAEIOU'
    result = ""
    for i in range(len(word) - 2, 0, -1):
        if word[i] in vowels and word[i - 1] not in vowels and word[i + 1] not in vowels:
            return word[i]
    return result