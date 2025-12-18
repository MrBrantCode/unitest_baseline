"""
QUESTION:
Create a function `add_strings(str1, str2)` that concatenates two input strings `str1` and `str2`. Each string can be up to 100 characters long and contain alphanumeric characters and special characters. The function should remove any leading or trailing whitespace from the input strings before concatenating them. If either string is null or empty, the function should return an error message.
"""

def entrance(str1, str2):
    # Check if either string is null or empty
    if not str1 or not str2:
        return "Error: Both input strings must not be null or empty."

    # Remove leading and trailing whitespace
    str1 = str1.strip()
    str2 = str2.strip()

    # Concatenate the strings
    return str1 + str2