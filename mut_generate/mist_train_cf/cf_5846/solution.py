"""
QUESTION:
Write a function called `format_sentence` that takes a string as input and returns a sentence in the format "Hello, [name]! How are you doing today?" The function should meet the following requirements: 

- It should check if the input string contains only alphabetic characters, spaces, hyphens, and periods, and display an error message and terminate if it contains any other characters.
- It should be case-insensitive when checking the input string for alphabetic characters.
- It should remove any leading or trailing whitespace from the input string before processing it.
- It should handle empty strings, strings with only whitespace characters, and strings with consecutive whitespace characters.
- It should capitalize the first letter of the name in the output sentence, including names with multiple words and names with mixed case.
- It should handle names with special characters, prefixes, suffixes, and hyphens.
- The time complexity of the function should be O(n), where n is the length of the input string.
"""

import re

def format_sentence(input_string):
    # Check for empty or whitespace-only strings
    if not input_string or input_string.isspace():
        print("Error: Input string cannot be empty or contain only whitespace characters.")
        return

    # Remove leading and trailing whitespace
    input_string = input_string.strip()

    # Check if input string contains only alphabetic characters
    if not re.match(r'^[a-zA-Z\s.-]+$', input_string):
        print("Error: Input string contains invalid characters. Only alphabetic characters, spaces, hyphens, and periods are allowed.")
        return

    # Capitalize the first letter of each word in the input string
    formatted_string = ' '.join(word.capitalize() for word in input_string.split())

    # Format the output sentence
    output_sentence = "Hello, {}! How are you doing today?".format(formatted_string)

    return output_sentence