"""
QUESTION:
Create a function called `remove_duplicates` that takes a string `input_string` as input, removes duplicate characters while ignoring case sensitivity, and returns a new string containing only unique characters sorted alphabetically. The function should be able to handle strings of varying sizes and special cases.
"""

def remove_duplicates(input_string):
    input_string = input_string.lower()
    unique_dict = {}
    for char in input_string:
        if char in unique_dict:
            continue
        else:
            unique_dict[char] = True
    unique_chars = sorted(list(unique_dict.keys()))
    new_string = ''.join(unique_chars)
    return new_string