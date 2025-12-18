"""
QUESTION:
Write a function named `normalize_text` that takes a string input, removes all whitespace characters, converts the string to lowercase, and replaces all non-alphanumeric characters with underscores.
"""

def normalize_text(text):
    # Remove whitespace
    text_without_spaces = text.replace(" ", "")

    # Convert to lowercase
    lower_case_text = text_without_spaces.lower()

    # Replace non-alphanumeric characters with underscores
    normalized_text = ''
    for character in lower_case_text:
        if character.isalnum():
            normalized_text += character
        else:
            normalized_text += "_"

    return normalized_text