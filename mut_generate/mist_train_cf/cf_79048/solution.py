"""
QUESTION:
Write a function `remove_strings(input_list)` that takes a list of strings as input and returns a new list containing only the strings that do not include the phrase "despite the fact that".
"""

def remove_strings(input_list):
    return [s for s in input_list if "despite the fact that" not in s.lower()]