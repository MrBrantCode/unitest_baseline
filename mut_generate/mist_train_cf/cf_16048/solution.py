"""
QUESTION:
Write a function `remove_string(string_to_remove, string_to_modify)` that takes two strings as input and returns a string where all occurrences of `string_to_remove` (case-insensitive) are removed from `string_to_modify` while preserving the original case sensitivity of `string_to_modify`. The function should also replace any occurrence of `string_to_remove` within another word with an empty string.
"""

def remove_string(string_to_remove, string_to_modify):
    # Convert both strings to lowercase for case-insensitive comparison
    lower_string_to_remove = string_to_remove.lower()
    lower_string_to_modify = string_to_modify.lower()

    # Split the string to modify into words
    words = string_to_modify.split()

    # Remove the string to remove from the words list
    modified_words = [word for word in words if word.lower() != lower_string_to_remove]

    # Join the modified words list into a string with spaces between words
    modified_string = ' '.join(modified_words)

    return modified_string