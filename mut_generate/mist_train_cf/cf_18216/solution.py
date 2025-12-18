"""
QUESTION:
Create a function `remove_empty_strings` that takes a list of strings as input and returns a new list containing only the non-empty strings from the original list, in the same order, without using any built-in string or list methods.
"""

def remove_empty_strings(input_list):
    new_list = []
    for element in input_list:
        if element != "":
            new_list.append(element)
    return new_list