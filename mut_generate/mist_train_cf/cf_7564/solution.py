"""
QUESTION:
Implement a function called "unique_list" that takes a list of integers as input and returns a new list containing unique integers from the input list, maintaining the order of the first occurrence of each integer. The function should not use any built-in functions, libraries, sets, or dictionaries, and should handle cases with empty lists, single-element lists, negative integers, and zero.
"""

def unique_list(input_list):
    unique_elements = []
    seen_elements = []

    for element in input_list:
        if element not in seen_elements:
            unique_elements.append(element)
            seen_elements.append(element)

    return unique_elements