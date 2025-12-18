"""
QUESTION:
Design a function named `find_longest_element` that takes a list of integers and/or floating-point numbers as input. The function should return the longest string representation of an element in the list and its corresponding index. The function should be able to handle both negative and positive numbers.
"""

def find_longest_element(lst):
    longest_element = None
    longest_length = 0
    longest_index = None

    for i, element in enumerate(lst):
        element_str = str(element)
        element_length = len(element_str)

        if element_length > longest_length:
            longest_element = element_str
            longest_length = element_length
            longest_index = i

    return longest_element, longest_index