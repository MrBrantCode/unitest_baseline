"""
QUESTION:
Create a function `create_strings_from_dict` that transforms the key-value pairs of a given dictionary into a list of strings. Each string should follow the format 'key: value'. The function should return the list of strings sorted in descending order of their lengths. If multiple strings have the same length, they should be sorted lexicographically. 

The input dictionary is expected to be non-empty and contain string keys and values. The function should handle edge cases such as empty dictionaries and non-dictionary inputs, returning error messages in these cases.
"""

def create_strings_from_dict(input_dict):
    # Validate the input and check if it is a dictionary
    if not isinstance(input_dict, dict):
        return "Input should be a dictionary."

    # Check if the dictionary is empty
    if not input_dict:
        return "Empty dictionary. Please provide a dictionary with some key-value pairs."

    all_strings = [f"{key}: {value}" for key, value in input_dict.items()]
    all_strings.sort()
    all_strings.sort(key=len, reverse=True)

    return all_strings