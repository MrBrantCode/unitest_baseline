"""
QUESTION:
Write a function `sum_of_lowercase_vowels` that calculates the sum of the ASCII values of all lowercase vowels in a given string, excluding any non-alphabetic characters. The function should return an integer value representing this sum.
"""

def sum_of_lowercase_vowels(string):
    """
    Calculate the sum of ASCII values of all lowercase vowels in a given string, 
    excluding any non-alphabetic characters.

    Args:
        string (str): Input string.

    Returns:
        int: Sum of ASCII values of lowercase vowels.
    """
    vowels = "aeiou"
    total = 0
    
    for char in string:
        if char.isalpha() and char.islower() and char in vowels:
            total += ord(char)
    
    return total