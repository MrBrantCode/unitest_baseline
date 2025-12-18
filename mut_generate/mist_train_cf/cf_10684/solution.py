"""
QUESTION:
Implement a function `reverse_dictionary(dictionary)` that takes a dictionary with at least 5 key-value pairs as input and returns a new dictionary with all keys and values reversed. The function should ensure that all keys and values are of type string. If a value is a dictionary, the function should recursively reverse its contents.
"""

def reverse_dictionary(dictionary):
    # Create a new empty dictionary to store the reversed contents
    reversed_dict = {}

    # Iterate over each key-value pair in the input dictionary
    for key, value in dictionary.items():
        # Convert the key and value to strings
        key_str = str(key)
        value_str = str(value)

        # Check if the value is a dictionary
        if isinstance(value, dict):
            # If it is a dictionary, recursively reverse its contents
            reversed_value = reverse_dictionary(value)
        else:
            # If it is not a dictionary, just reverse the string
            reversed_value = value_str[::-1]

        # Reverse the key as well
        reversed_key = key_str[::-1]

        # Add the reversed key-value pair to the new dictionary
        reversed_dict[reversed_key] = reversed_value

    # Return the reversed dictionary
    return reversed_dict