"""
QUESTION:
Design a function `find_unique_elements` that takes a list of integers as input and returns a list of elements that do not have an equivalent value with an opposite sign in the input list. The function should ignore elements that have a corresponding inversely signed counterpart.
"""

def find_unique_elements(sample_list):
    # Creating an empty list to capture unique elements
    unique_elements = []

    # Iterating through the given list
    for i in sample_list:
        # Looking for inversely signed counterpart.       
        if -i not in sample_list:
            unique_elements.append(i)

    # Returning the output.
    return unique_elements