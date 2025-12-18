"""
QUESTION:
Write a function `parse_data` that takes a string representing a series of key-value pairs enclosed in curly braces and returns a dictionary mapping each key to its corresponding value. The input string will always be well-formed, with keys as alphanumeric strings enclosed in single quotes, followed by a colon, and then the corresponding integer value. The input string may contain whitespace characters, but they should be ignored during parsing.
"""

def parse_data(data: str) -> dict:
    data = data.strip('{}')  # Remove the outer curly braces
    pairs = data.split(',')  # Split the string into individual key-value pairs
    result = {}
    for pair in pairs:
        key, value = pair.split(':')  # Split each pair into key and value
        key = key.strip().strip("'")  # Remove leading/trailing whitespace and single quotes from the key
        value = int(value.strip())  # Convert the value to an integer after removing leading/trailing whitespace
        result[key] = value  # Add the key-value pair to the result dictionary
    return result