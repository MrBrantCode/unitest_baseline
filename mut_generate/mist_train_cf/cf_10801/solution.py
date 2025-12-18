"""
QUESTION:
Create a function named `string_length_dict` that takes a list of strings as input and returns a dictionary. The dictionary should have the input strings as keys and their lengths as values, but it should only include the first occurrence of each string and ignore any strings containing numbers or special characters.
"""

def string_length_dict(strings):
    length_dict = {}
    for string in strings:
        # Check if string contains numbers or special characters
        if any(char.isdigit() or not char.isalnum() for char in string):
            continue
        # Add string to dictionary only if it is not already present
        if string not in length_dict:
            length_dict[string] = len(string)
    return length_dict