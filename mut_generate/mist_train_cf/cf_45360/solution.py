"""
QUESTION:
Write an iterative function `longest_substring(input_string)` that finds the longest unbroken sequence of a single unique character in a given string, handling both ASCII and Unicode characters. The function should return the longest substring of consecutive identical characters, including the case where a single character forms the longest repeated sequence.
"""

def longest_substring(input_string):
    if not input_string:  # handle empty string
        return ''

    longest_substr = current_substr = input_string[0]
    for char in input_string[1:]:
        if char == current_substr[0]:
            current_substr += char
        else:
            if len(current_substr) > len(longest_substr):
                longest_substr = current_substr
            current_substr = char

    # Check if the last substring was the longest one
    if len(current_substr) > len(longest_substr):
        longest_substr = current_substr

    return longest_substr