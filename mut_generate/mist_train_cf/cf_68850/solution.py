"""
QUESTION:
Create a function `get_palindrome_substrings` that takes a string `input_string` as input and returns a list of all unique palindrome substrings in the input string. The function should be able to handle strings of any length, but note that generating all substrings for very long strings may be memory-intensive.
"""

def get_palindrome_substrings(input_string):
    length = len(input_string)
    all_sub_strings = [input_string[i: j] for i in range(length) for j in range(i + 1, length + 1)]
    return [str for str in all_sub_strings if str == str[::-1]]