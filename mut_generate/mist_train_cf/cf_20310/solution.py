"""
QUESTION:
Create a function `validate_input` that takes two parameters: a number `num` and a string `string`. The function should return an array with `num` and `string` if the following conditions are met: `num` is between -1000 and 1000 (inclusive) and `string` is at least 10 characters long and contains only alphabetical characters. Otherwise, the function should return an empty array.
"""

def validate_input(num, string):
    # Check if number is within the range -1000 to 1000 (inclusive)
    if num < -1000 or num > 1000:
        return []

    # Check if string is valid and contains only alphabetical characters
    if len(string) < 10 or not string.isalpha():
        return []

    # Return an array with the number and string
    return [num, string]