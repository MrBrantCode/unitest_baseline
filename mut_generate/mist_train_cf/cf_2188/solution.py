"""
QUESTION:
Create a function called `filter_string` that takes two parameters: `string` and `max_length`. The function should return a list of characters, where each character is an uppercase letter from the input string converted to lowercase. The function should ignore non-uppercase letters and ensure the length of the output list does not exceed `max_length`.
"""

def filter_string(string, max_length):
    result = []
    for char in string:
        if char.isupper():
            result.append(char.lower())
            if len(result) == max_length:
                break
    return result