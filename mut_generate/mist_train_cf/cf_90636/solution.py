"""
QUESTION:
Design a function named `find_longest_element` that takes a list of elements as input, where elements can be negative numbers, floating-point numbers, or integers. The function should return the longest element and its index in the list, considering the length of the element as a string.
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