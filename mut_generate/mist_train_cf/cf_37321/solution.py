"""
QUESTION:
Implement a function `validate_input(input_string)` that takes a string `input_string` as input and returns a boolean value indicating whether the input string is valid or not. The input string is valid if it meets the following conditions:
- The length of the input string is 10 characters.
- The input string contains exactly 2 occurrences of the letter 'A' and 3 occurrences of the letter 'N' (case-sensitive).
- The input string does not contain any repeated characters.
The function should return True if the input string is valid and False otherwise.
"""

def validate_input(input_string: str) -> bool:
    if len(input_string) != 10:
        return False

    if input_string.count('A') != 2 or input_string.count('N') != 3:
        return False

    for char in input_string:
        if input_string.count(char) > 1:
            return False

    return True