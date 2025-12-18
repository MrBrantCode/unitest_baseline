"""
QUESTION:
Create a function `add_strings(str1, str2)` that takes two input strings, removes any leading or trailing whitespace, and returns their concatenation. The function should handle cases where one or both of the input strings are null or empty, returning an error message instead. The function should be able to handle strings of up to 10^6 characters and run in O(n) time complexity, where n is the total length of both input strings.
"""

def add_strings(str1, str2):
    # Check for null or empty strings
    if str1 is None or str2 is None or str1 == '' or str2 == '':
        return 'Error: Input strings cannot be null or empty'

    # Remove leading and trailing whitespace
    str1 = str1.strip()
    str2 = str2.strip()

    # Concatenate the strings
    result = str1 + str2

    return result