"""
QUESTION:
Create a function `find_min_string` that takes an array of diverse elements as input, including both digits and alphabets, and returns the smallest alphanumeric string. The smallest string is determined by the ASCII order, where digits have lesser value than alphabets. If the array does not contain any alphanumeric strings, the function should return `None`.
"""

def find_min_string(arr):
    # Filter array to only contain alphanumeric strings
    alphanumeric_strings = [s for s in arr if s.isalnum()]

    # If there are no alphanumeric strings, return None
    if not alphanumeric_strings:
        return None

    # Sort the strings by ASCII value
    alphanumeric_strings.sort()

    # Return the first string, which is the smallest
    return alphanumeric_strings[0]