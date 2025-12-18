"""
QUESTION:
Create a function `filter_string` that takes in a string `string` and a maximum length `max_length`. The function should return an array of characters that includes only the lowercase versions of the uppercase letters from the input string, truncated to the specified maximum length.
"""

def filter_string(string, max_length):
    result = []
    for char in string:
        if char.isupper():
            result.append(char.lower())
            if len(result) == max_length:
                break
    return result