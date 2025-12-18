"""
QUESTION:
Create a function called `filter_strings` that takes a list of strings as input and returns a new list containing only the strings that have a length greater than 5 characters and start with the letter 'A'. If no strings meet these criteria, the function should return an empty list.
"""

def filter_strings(input_list):
    return [string for string in input_list if len(string) > 5 and string.startswith('A')]