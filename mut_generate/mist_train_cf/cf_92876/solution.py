"""
QUESTION:
Write a function called `filter_strings` that takes a list of strings as input and returns a new list containing only the strings that have a length greater than 4 and at least one uppercase letter.
"""

def filter_strings(lst):
    new_lst = []
    for string in lst:
        if len(string) > 4 and any(char.isupper() for char in string):
            new_lst.append(string)
    return new_lst