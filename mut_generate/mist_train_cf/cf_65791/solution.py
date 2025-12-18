"""
QUESTION:
Implement a function named `merge_dictionaries` that takes two dictionaries as input and returns a new dictionary. The new dictionary should only include the keys that are present in both input dictionaries with the value as a tuple containing the corresponding values from both dictionaries for the common keys.
"""

def merge_dictionaries(given_dictionary, predefined_dictionary):
    # Initialize the result dictionary
    result = {}

    # Iterate over keys in the given dictionary
    for key in given_dictionary.keys():
        # Check if key is also in predefined_dictionary
        if key in predefined_dictionary:
            # If so, add the key and a tuple of values to the result
            result[key] = (given_dictionary[key], predefined_dictionary[key])

    # Return the result
    return result