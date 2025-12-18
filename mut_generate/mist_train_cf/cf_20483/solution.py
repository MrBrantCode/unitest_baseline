"""
QUESTION:
Write a function `format_sentence` that takes a string as input, checks if it contains only alphabetic characters (case-insensitive), removes leading/trailing whitespace, capitalizes the first letter of each word, and returns a formatted sentence in the style "Hello, [name]! How are you doing today?" If the input string contains non-alphabetic characters, the function should display an error message and terminate. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def format_sentence(input_string):
    # Remove leading and trailing whitespace
    input_string = input_string.strip()

    # Check if the input string contains only alphabetic characters
    if not input_string.replace(" ", "").isalpha():
        print("Error: Input string should contain only alphabetic characters.")
        return

    # Capitalize the first letter of each word in the input string
    name = input_string.title()

    # Format and return the output sentence
    return f"Hello, {name}! How are you doing today?"