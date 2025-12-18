"""
QUESTION:
Create a function named `count_letters` that takes a string of text as input and returns a dictionary containing the number of occurrences of each letter in the string, ignoring whitespace and being case-insensitive.
"""

def count_letters(text):
    """
    Returns a dictionary containing the number of occurrences of each letter in the string, 
    ignoring whitespace and being case-insensitive.

    Args:
    text (str): The input string.

    Returns:
    dict: A dictionary where keys are letters and values are their respective counts.
    """
    text = text.lower().replace(' ', '')
    return {char: text.count(char) for char in set(text)}


def count_letters_optimized(text):
    """
    Returns a dictionary containing the number of occurrences of each letter in the string, 
    ignoring whitespace and being case-insensitive. This function is optimized for performance.

    Args:
    text (str): The input string.

    Returns:
    dict: A dictionary where keys are letters and values are their respective counts.
    """
    counter = {}
    for char in text.lower():
        if char != ' ':
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
    return counter