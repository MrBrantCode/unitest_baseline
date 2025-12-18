"""
QUESTION:
Write a function `get_fifth_letter(string)` that takes a string as input, ignores whitespace characters, and returns the fifth letter of the string. If the string has less than five letters, the function should return "Error: String has less than 5 letters." If the string contains any special characters, the function should return "Error: String contains special characters."
"""

def get_fifth_letter(string):
    # Remove whitespace characters
    string = string.replace(" ", "")

    # Check if string length is less than 5
    if len(string) < 5:
        return "Error: String has less than 5 letters."

    # Check if string contains special characters
    if not string.isalnum():
        return "Error: String contains special characters."

    # Return the fifth letter of the string
    return string[4]