"""
QUESTION:
Create a function `char_frequency` that takes a string as input and returns the frequency of each alphabet character in the string, ignoring case sensitivity and non-alphabet characters. The output should be a dictionary sorted in ascending order of the characters' ASCII values.
"""

def char_frequency(s):
    """
    Returns the frequency of each alphabet character in the string, 
    ignoring case sensitivity and non-alphabet characters.
    
    Args:
        s (str): The input string.
    
    Returns:
        dict: A dictionary containing the frequency of each alphabet character.
    """
    freq_dict = {}
    for char in s.lower():
        if char.isalpha():
            if char in freq_dict:
                freq_dict[char] += 1
            else:
                freq_dict[char] = 1
    return dict(sorted(freq_dict.items()))