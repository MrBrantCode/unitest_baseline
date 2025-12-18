"""
QUESTION:
Write a function `char_frequency` that calculates the frequency of each alphabet character in a given string, ignoring case sensitivity and non-alphabetic characters. The output should be sorted in descending order of the characters' ASCII values.

The function should take one argument: a string. It should return a dictionary or print the frequency of each character in descending order of ASCII values. The function should handle non-alphabetic characters appropriately.
"""

def char_frequency(s):
    """
    Calculate the frequency of each alphabet character in a given string, 
    ignoring case sensitivity and non-alphabetic characters.
    
    Args:
    s (str): The input string.
    
    Returns:
    dict: A dictionary with characters as keys and their frequencies as values, 
          sorted in descending order of the characters' ASCII values.
    """
    s = s.lower()
    frequency = {}
    for char in s:
        if char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
    sorted_chars = sorted(frequency.keys(), key=lambda x: ord(x), reverse=True)
    sorted_frequency = {char: frequency[char] for char in sorted_chars}
    return sorted_frequency