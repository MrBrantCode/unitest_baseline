"""
QUESTION:
Create a function named `character_frequency` that takes a string as input and returns a dictionary containing the frequency of each unique character in the string. The function should ignore case sensitivity and whitespace characters. The function should have a time complexity of O(n), where n is the length of the string.
"""

def character_frequency(string):
    # Create an empty dictionary to store the character frequencies
    frequency_dict = {}

    # Remove whitespace characters from the string
    string = string.replace(" ", "")

    # Convert the string to lowercase to ignore case sensitivity
    string = string.lower()

    # Iterate through each character in the string
    for char in string:
        # Check if the character is already in the dictionary
        if char in frequency_dict:
            # If so, increment its frequency by 1
            frequency_dict[char] += 1
        else:
            # If not, add the character to the dictionary with a frequency of 1
            frequency_dict[char] = 1

    # Return the dictionary of character frequencies
    return frequency_dict