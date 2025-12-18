"""
QUESTION:
Create a function `find_combinations(input_string, desired_length)` that generates all unique combinations of letters from a given string, excluding non-alphabetic characters and repeated characters within each combination. The combinations should be of a specified length defined by the user, and the order of the characters does not matter. The function should efficiently handle strings up to a length of 1000.
"""

from itertools import combinations
import string

def find_combinations(input_string, desired_length):
    # Filtering out the input string to only include letters:
    input_string = ''.join(filter(str.isalpha, input_string))

    # If the string is empty or desired length is 0, return an empty list:
    if not input_string or desired_length == 0:
        return []

    # If the length of unique characters in the string is smaller than the desired length, return an empty list:
    if len(set(input_string)) < desired_length:
        return []

    # Otherwise, generate all combinations:
    result = set(combinations(input_string, desired_length))

    # Format the result, remove duplicates and sort it:
    result = sorted([''.join(sorted(set(item))) for item in result if len(set(item)) == desired_length])

    return result