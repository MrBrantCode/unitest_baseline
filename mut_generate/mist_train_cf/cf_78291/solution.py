"""
QUESTION:
Implement a function named `filter_by_char` that takes in an array of strings and a single alphabetic character as a filter, and returns an array of strings that include the filter character. Ensure that the function includes error checking to handle cases where the filter is not a single alphabetic character, the filter is not a string, or the array contains non-string elements. If any of these error conditions are met, return a corresponding error message.
"""

def filter_by_char(array, filter):
    if not isinstance(filter, str):
        return 'Error: Filter must be a string'
    if not filter.isalpha():
        return 'Error: Filter must be alphabetic'
    if len(filter) > 1:
        return 'Error: Filter must be a single character'

    result = []
    for word in array:
        if not isinstance(word, str):
            return 'Error: All items in array must be strings'
        if filter in word:
            result.append(word)
    return result