"""
QUESTION:
Write a function `string_to_list` that takes a string as input and returns a list of characters, excluding whitespace characters. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in string or list methods, regular expressions, or third-party libraries. The function should correctly handle strings with leading or trailing whitespace characters.
"""

def string_to_list(string):
    # Remove leading and trailing whitespace characters
    string = string.strip()

    # Initialize an empty list to store the characters
    char_list = []

    # Iterate over each character in the string
    for char in string:
        # Check if the character is not a whitespace character
        if char != ' ':
            # Append the character to the list
            char_list.append(char)

    return char_list