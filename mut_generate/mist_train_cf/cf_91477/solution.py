"""
QUESTION:
Implement a function named `reverse_dictionary` that takes a dictionary as input and returns a new dictionary with all key-value pairs reversed. Ensure that all keys and values in the resulting dictionary are of type string. If a value is a nested dictionary, recursively reverse its contents. The input dictionary must have at least 5 key-value pairs.
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