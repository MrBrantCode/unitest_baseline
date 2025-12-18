"""
QUESTION:
Implement a function `character_indices` that takes a string as input and returns a dictionary where each key is a character from the string and its corresponding value is a list of indices where the character appears in the string. The function should only include characters that appear more than once in the string and sort the dictionary in descending order by characters. The time complexity should not exceed O(n^2), where n is the length of the string.
"""

def character_indices(string):
    char_dict = {}
    repeated_chars = set()

    # Iterate through the string
    for index, char in enumerate(string):
        # Check if character is already in the dictionary
        if char in char_dict:
            # Add index to the character's list
            char_dict[char].append(index)
            # Add character to the set of repeated characters
            repeated_chars.add(char)
        else:
            # Initialize the character's list with the current index
            char_dict[char] = [index]

    # Sort the dictionary in descending order by characters
    sorted_dict = dict(sorted(char_dict.items(), reverse=True))

    # Filter the dictionary to include only characters that appear more than once
    filtered_dict = {char: indices for char, indices in sorted_dict.items() if char in repeated_chars}

    return filtered_dict