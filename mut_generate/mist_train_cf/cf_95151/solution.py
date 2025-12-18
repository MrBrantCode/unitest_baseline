"""
QUESTION:
Create a function named `parse_string` that takes a string of key/value pairs as input, where each pair is separated by a newline character. The keys and values can contain alphanumeric characters, special characters, and spaces. The function should return a dictionary where the keys are case-sensitive and the values are paired with the corresponding keys. If there are duplicate keys, the value associated with the last occurrence of the key should be stored in the dictionary. Leading and trailing spaces in each line should be ignored, and empty lines or lines without an equal sign should be ignored during parsing.
"""

def parse_string(input_string):
    # Initialize an empty dictionary to store the key-value pairs
    result = {}

    # Split the input string into lines
    lines = input_string.split('\n')

    # Iterate through each line
    for line in lines:
        # Remove leading and trailing spaces from the line
        line = line.strip()

        # Ignore empty lines
        if not line:
            continue

        # Split the line at the first occurrence of '='
        parts = line.split('=', 1)

        # Ignore lines without '='
        if len(parts) != 2:
            continue

        # Extract the key and value from the parts
        key, value = parts

        # Remove leading and trailing spaces from the key and value
        key = key.strip()
        value = value.strip()

        # Check if the key is enclosed in quotes
        if key.startswith('"') and key.endswith('"'):
            key = key[1:-1]  # Remove the quotes

        # Check if the value is enclosed in quotes
        if value.startswith('"') and value.endswith('"'):
            value = value[1:-1]  # Remove the quotes

        # Store the value in the dictionary, overwriting any previous value for the same key
        result[key] = value

    return result