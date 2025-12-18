"""
QUESTION:
Create a function named `get_unique_characters` that takes a string as input and returns a list of unique characters. The returned list should be sorted in descending order based on character frequency. In cases of equal frequency, characters should be sorted alphabetically. The function should exclude whitespace and punctuation marks from the input string.
"""

import string

def entrance(input_str):
    # Remove whitespace and punctuation marks from the string
    input_str = ''.join(char for char in input_str if char not in string.whitespace and char not in string.punctuation)
    
    # Create a dictionary to store the frequency of each character
    frequency_dict = {}
    
    # Count the frequency of each character
    for char in input_str:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    # Sort the characters based on their frequency in descending order
    sorted_characters = sorted(frequency_dict.keys(), key=lambda x: (-frequency_dict[x], x))
    
    # Return the list of unique characters sorted by their frequency
    return sorted_characters