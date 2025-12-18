"""
QUESTION:
Implement a function named `get_chars` that takes a list of strings as input and returns a dictionary. The function should map each input string to a list of its 9th, 10th, and 11th characters. If a string has fewer than 11 characters, replace the missing characters with a unique identifier 'Unique Identifier'. The function should also handle non-string inputs by returning an error message for each invalid input.
"""

def get_chars(strings):
    result = {}
    for string in strings:
        # check if it is a string
        if not isinstance(string, str):
            result[string] = f"Error: {string} is not a string."
        else:
            # get 9th, 10th and 11th characters
            chars = [string[i] if i < len(string) else 'Unique Identifier' for i in range(8, 11)]
            result[string] = chars
    return result