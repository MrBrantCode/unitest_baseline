"""
QUESTION:
Write a function `get_fifth_letter` that takes a string as input, removes all whitespace characters, and returns the fifth letter of the resulting string. If the resulting string has less than five letters, the function should return an error message "Error: The string has less than five letters."
"""

def get_fifth_letter(string):
    string = string.replace(" ", "")
    if len(string) < 5:
        return "Error: The string has less than five letters."
    return string[4]