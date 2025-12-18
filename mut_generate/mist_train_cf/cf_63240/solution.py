"""
QUESTION:
Write a function `remove_strings` that takes a list of strings as input and returns a new list containing only the strings that do not include the phrase "regardless of".
"""

def remove_strings(input_list):
    output_list = [phrase for phrase in input_list if 'regardless of' not in phrase]
    return output_list