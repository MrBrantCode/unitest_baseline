"""
QUESTION:
Write a function `display_consonants` that takes a string as input and displays each consonant in the string one at a time, excluding vowels and spaces, ignoring uppercase and lowercase distinctions. The function should also return the total count of consonants in the string.
"""

def display_consonants(s):
    """
    Displays each consonant in the input string one at a time, excluding vowels and spaces, 
    ignoring uppercase and lowercase distinctions. Returns the total count of consonants in the string.

    Parameters:
    s (str): The input string.

    Returns:
    int: The total count of consonants in the string.
    """
    consonant_count = 0
    vowels = 'aeiou'
    for char in s.lower():
        if char.isalpha() and char not in vowels:
            print(char)
            consonant_count += 1
    return consonant_count