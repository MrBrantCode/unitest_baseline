"""
QUESTION:
Design a function named `concatenate_strings` that takes two strings as input, `string1` and `string2`, and returns a string containing the alphabetical characters from both strings. The output string should be in alphabetical order and not contain any duplicate characters. The function should ignore any non-alphabetical characters and be case-insensitive, treating both uppercase and lowercase characters as the same.
"""

def concatenate_strings(string1, string2):
    # Extract alphabetical characters from both strings
    alpha_chars1 = [char.lower() for char in string1 if char.isalpha()]
    alpha_chars2 = [char.lower() for char in string2 if char.isalpha()]

    # Remove duplicates from both lists
    alpha_chars1 = list(set(alpha_chars1))
    alpha_chars2 = list(set(alpha_chars2))

    # Concatenate the two lists and sort them alphabetically
    result = sorted(alpha_chars1 + alpha_chars2)

    # Join the characters into a string and return it
    return ''.join(result)