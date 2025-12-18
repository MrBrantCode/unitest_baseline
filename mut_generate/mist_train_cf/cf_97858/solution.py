"""
QUESTION:
Create a function named `remove_duplicates` that takes an input string and returns a new string containing unique characters from the input string, sorted alphabetically and case-insensitive. The function should handle strings of varying sizes and ignore case sensitivity.
"""

def remove_duplicates(input_string):
    # Convert input string to lowercase or uppercase
    input_string = input_string.lower() 

    # Create an empty dictionary to store unique characters
    unique_dict = {}

    # Loop through each character in the string
    for char in input_string:
        # Check if the character is already in the dictionary
        if char in unique_dict:
            continue
        else:
            unique_dict[char] = True

    # Extract the unique characters and sort them alphabetically
    unique_chars = sorted(list(unique_dict.keys()))

    # Concatenate the unique characters to create a new string
    new_string = ''.join(unique_chars)

    return new_string