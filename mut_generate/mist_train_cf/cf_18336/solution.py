"""
QUESTION:
Create a function `parse_string` that takes an input string containing lines of key/value pairs and returns a dictionary of the values paired with the keys. The keys should be case-sensitive, and the value associated with the last occurrence of the key should be stored in the dictionary. The keys and values can contain alphanumeric characters as well as special characters. The function should ignore leading/trailing spaces, empty lines, and lines without an equal sign. It should also handle spaces within the key and/or value, escape characters, and quoted keys and values.
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