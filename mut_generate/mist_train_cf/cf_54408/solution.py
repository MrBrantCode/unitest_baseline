"""
QUESTION:
Construct a method `arrange_descending` that takes a list of alphanumeric strings as input and returns the list sorted in descending order based on their alphabetical value. The entire string, including numbers, should be considered for sorting.
"""

def arrange_descending(input_list):
    input_list.sort(reverse=True)
    return input_list