"""
QUESTION:
Create a function `char_frequency` that takes a string as input and returns a dictionary where the keys are distinct characters in the string and the values are the frequency of their occurrence. Consider both lower-case and upper-case letters as distinct characters and also take whitespaces and special characters into account. The function should have no restrictions on input string length and should work with any string.
"""

def char_frequency(text):
    """
    This function takes a string as input and returns a dictionary where the keys are distinct characters in the string 
    and the values are the frequency of their occurrence.

    Parameters:
    text (str): The input string.

    Returns:
    dict: A dictionary with distinct characters as keys and their frequency as values.
    """
    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq