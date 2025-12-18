"""
QUESTION:
Create a function named `unique_characters` that takes a string as input. The function should return a list of unique alphabetic characters in the string, sorted in descending order, with no duplicates. The input string should be preprocessed to remove non-alphabetic characters before extracting unique characters.
"""

def unique_characters(string):
    # Remove non-alphabetic characters from the string
    string = ''.join(char for char in string if char.isalpha())
    
    # Create a set of unique characters from the string
    unique_chars = set(string)
    
    # Sort the unique characters in descending order
    sorted_chars = sorted(unique_chars, reverse=True)
    
    # Return the sorted characters as a list
    return sorted_chars