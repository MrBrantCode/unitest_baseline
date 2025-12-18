"""
QUESTION:
Define a function named `advanced_vowels_count` that takes a string as an argument and returns the total count of all vowels it contains. The vowels to be considered are 'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'é', 'å', 'ä', 'ö', etc. The function should disregard case sensitivity and handle unconventional characters, null strings, numeric strings, and strings with whitespaces and punctuations.
"""

def advanced_vowels_count(word):
    """
    Define the function named advanced_vowels_count; this accepts a string denoting a word as an argument and returns the total count of all vowels it contains. The vowels considered here are 'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'é', 'å', 'ä', 'ö', etc. Disregard case sensitivity and handle unconventional characters included in the input string. Moreover, the function should also handle null strings, numeric strings, and strings with whitespaces and punctuations.
    """
    vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'é', 'å', 'ä', 'ö']
    count = 0
    for letter in word.lower():
        if letter in vowels:
            count += 1
    return count