"""
QUESTION:
Write a function named `count_chars` that takes a string as input and returns the counts of vowels, consonants, digits, and special characters in the string, excluding whitespace characters. The function should be case-insensitive when counting vowels and consonants.
"""

def count_chars(s):
    """
    Counts vowels, consonants, digits, and special characters in a string, excluding whitespace characters.

    Args:
        s (str): The input string.

    Returns:
        dict: A dictionary containing the counts of vowels, consonants, digits, and special characters.
    """
    vowels = 0
    consonants = 0
    digits = 0
    special_chars = 0

    for char in s:
        if char.isalpha() and char.lower() in "aeiou":
            vowels += 1
        elif char.isalpha():
            consonants += 1
        elif char.isdigit():
            digits += 1
        elif not char.isspace():
            special_chars += 1

    return {"vowels": vowels, "consonants": consonants, "digits": digits, "special_chars": special_chars}