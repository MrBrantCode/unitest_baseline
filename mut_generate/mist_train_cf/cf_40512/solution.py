"""
QUESTION:
Create a function named `character_frequency` that takes a string as input and returns a dictionary with the frequency of each character in the string, ignoring spaces and being case-insensitive. The function should treat uppercase and lowercase letters as the same character.
"""

def character_frequency(input_string: str) -> dict:
    # Remove spaces and convert the string to lowercase
    input_string = input_string.replace(" ", "").lower()
    
    # Initialize an empty dictionary to store character frequencies
    frequency_dict = {}
    
    # Iterate through the characters in the input string
    for char in input_string:
        # Increment the frequency count for each character
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    
    return frequency_dict