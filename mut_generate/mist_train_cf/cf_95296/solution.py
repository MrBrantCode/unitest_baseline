"""
QUESTION:
Create a function named `convert_array_to_string` that takes an array of characters as input. The function should return a string containing only the alphabetic characters from the input array, sorted in ascending order. Non-alphabetic characters and the original order of the characters should be ignored.
"""

def convert_array_to_string(array):
    # Filter out non-alphabetic characters
    alphabetic_chars = [char for char in array if char.isalpha()]
    
    # Sort the alphabetic characters in ascending order
    sorted_chars = sorted(alphabetic_chars)
    
    # Join the sorted characters into a string
    result = ''.join(sorted_chars)
    
    return result