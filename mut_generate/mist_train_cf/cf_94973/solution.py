"""
QUESTION:
Create a function named `concatenate_strings` that takes two strings as input. The function should remove any leading or trailing white spaces from both strings and concatenate them. If either string is empty after removing white spaces, or if the concatenated string contains any numeric digits, the function should return an error message. Otherwise, it should return the concatenated string.
"""

def concatenate_strings(string1, string2):
    string1 = string1.strip()
    string2 = string2.strip()

    if not string1 or not string2:
        return "Error: Input strings cannot be empty"

    concatenated_string = string1 + string2

    if any(char.isdigit() for char in concatenated_string):
        return "Error: Input strings cannot contain numbers"

    return concatenated_string