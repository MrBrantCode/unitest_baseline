"""
QUESTION:
Write a function `count_characters` that takes a string as an input and returns a dictionary with each alphanumeric character from the string as a key and their corresponding count as the value. The function should handle edge cases where the input string is `None` and return an empty dictionary. Non-alphanumeric characters should be ignored.
"""

def count_characters(input_string):
    # Check edge case for null input
    if input_string is None:
        return {}

    # Construct the count dictionary
    result_dict = {}
    for char in input_string:
        # Ignore white space and special characters
        if char.isalnum():
            char_lower = char.lower()
            if char_lower in result_dict:
                result_dict[char_lower] += 1
            else:
                result_dict[char_lower] = 1
    return result_dict