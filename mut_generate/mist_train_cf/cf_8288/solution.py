"""
QUESTION:
Write a function `convert_string_to_list` that takes a string as input. The function should remove leading and trailing whitespace characters from the string, then check if the resulting string's length is greater than 10 characters and contains at least one uppercase letter. If both conditions are met, convert the string to a list of characters; otherwise, return None.
"""

def convert_string_to_list(string):
    string = string.strip()
    if len(string) <= 10 or not any(char.isupper() for char in string):
        return None
    else:
        return list(string)