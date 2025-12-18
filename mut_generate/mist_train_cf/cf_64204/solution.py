"""
QUESTION:
Create a function named `advanced_transformation` that accepts a string `sequence` as input. The function should perform the following operations: 
- Reverse the capitalization of all letters in the string.
- Modify all numeric characters to the next nearest even number.
- Double all special characters in the string.
- Count the frequency of each character after these transformations.

The function should return a dictionary containing the transformed string and another dictionary with the frequency of each character in the transformed string.
"""

def advanced_transformation(sequence: str) -> dict:
    # Define a mapping for numbers to their nearest even equivalent
    number_mapping = {'1': '0', '3': '2', '5': '4', '7': '6', '9': '8'}
    
    # Initialize an empty string to capture the transformed sequence
    transformed_sequence = ''
    
    # Process each character in the sequence
    for char in sequence:
        # If it is a number, map it to nearest even number. Otherwise convert to opposite case.
        if char.isdigit():
            transformed_sequence += number_mapping.get(char, char)
        else:
            transformed_sequence += char.swapcase()
            if not char.isalnum():
                # If it is special character, double it
                transformed_sequence += char

    # Initialise an empty dict to capture the frequency
    result_dict = {}

    # Process each character in the transformed_sequence to calculate frequency
    for char in transformed_sequence:
        # Increase the count in the dict for each character occurrence
        if char in result_dict:
            result_dict[char] += 1
        else:
            result_dict[char] = 1

    # Return the resulting dict
    return {'transformed_sequence': transformed_sequence, 'frequency_dict': result_dict}