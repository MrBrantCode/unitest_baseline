"""
QUESTION:
Write a function named `switch_case` that takes a character as input and performs different operations based on the character. The function should return "Vowel" if the character is a vowel, "Space" if it's a space, and "Other" otherwise. Include a function named `count_characters` to count the frequency of every character in a given string. Also, write a `main` function that takes the string "Felis catus", counts the total characters, vowels, and spaces, and handles exceptions for alphanumeric characters and special symbols by printing an error message. The function should also print the count of every character in the string, excluding non-alphabetic characters and special symbols.
"""

def switch_case(char):
    """
    This function simulates a switch-case structure to perform different operations based on the character.
    It returns "Vowel" if the character is a vowel, "Space" if it's a space, and "Other" otherwise.

    Args:
        char (str): A single character to be checked.

    Returns:
        str: "Vowel" if char is a vowel, "Space" if it's a space, and "Other" otherwise.
    """
    switcher = {
        'a': "Vowel",
        'e': "Vowel",
        'i': "Vowel",
        'o': "Vowel",
        'u': "Vowel",
        ' ': "Space",
    }
    return switcher.get(char, "Other")