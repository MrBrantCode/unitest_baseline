"""
QUESTION:
Write a function `transformString` that takes a string as input and returns the transformed string with all substrings enclosed within single quotes converted to uppercase and the single quotes removed. The function should handle multiple occurrences of the pattern in the input string.
"""

def transformString(input_string):
    transformed_string = input_string
    start_index = transformed_string.find("'")
    while start_index != -1:
        end_index = transformed_string.find("'", start_index + 1)
        if end_index != -1:
            substring_to_replace = transformed_string[start_index + 1:end_index]
            transformed_string = transformed_string.replace(
                f"'{substring_to_replace}'", substring_to_replace.upper()
            )
            start_index = transformed_string.find("'", end_index + 1)
        else:
            break
    return transformed_string