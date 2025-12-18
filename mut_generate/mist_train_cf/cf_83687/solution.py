"""
QUESTION:
Create a function `character_tracker` that takes a string as input and returns a dictionary and a list. The dictionary should have characters (both uppercase and lowercase, digits, punctuation marks, and rare ASCII characters) as keys, and their corresponding values should be dictionaries with 'Count' and 'First Position' keys. 'Count' should represent the number of repetitions of the character in the string, and 'First Position' should represent the index of the character's first appearance in the string. The function should be case-insensitive, i.e., it should treat 'G' and 'g' as the same character. The list should contain the characters in the order of their first appearance in the string. The function should handle multiple character types, including alphabets, digits, punctuation marks, and rare ASCII characters.
"""

def character_tracker(input_string):
    # Define an empty dictionary
    output_dict = {}

    # Traverse each character in the string
    for idx, char in enumerate(input_string):
        # Lowercase the character for case insensitivity
        lower_char = char.lower()

        # If the character is already in the dictionary
        if lower_char in output_dict:
            # Increment its count
            output_dict[lower_char]["Count"] += 1
        # If the character is not in the dictionary yet
        else:
            # Add it and record its first position
            output_dict[lower_char] = {"Count": 1, "First Position": idx}

    # Create a sorted list based on first appearance
    sorted_keys = sorted(output_dict, key=lambda x: output_dict[x]["First Position"])

    return output_dict, sorted_keys