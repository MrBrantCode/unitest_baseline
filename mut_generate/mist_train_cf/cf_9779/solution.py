"""
QUESTION:
Write a function `count_vowel_words` that takes a string and an integer as arguments. The function should return the number of words in the string that start with a vowel (a, e, i, o, u) and are of the provided length.
"""

def count_vowel_words(string, length):
    """
    Returns the number of words in the string that start with a vowel (a, e, i, o, u) and are of the provided length.

    Args:
        string (str): The input string.
        length (int): The length of the words to be counted.

    Returns:
        int: The number of words that start with a vowel and are of the provided length.
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum(1 for word in string.split() if len(word) == length and word[0].lower() in vowels)