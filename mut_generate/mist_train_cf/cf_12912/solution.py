"""
QUESTION:
Write a function named `convert_to_floats` that takes an array of strings as input and returns a new array containing only the strings that can be successfully converted to floats. The function should ignore any strings that cannot be directly converted to floats.
"""

def convert_to_floats(string_arr):
    return [float(string) for string in string_arr if isinstance(string, str) and string.replace('.', '', 1).replace('-', '', 1).isdigit()]