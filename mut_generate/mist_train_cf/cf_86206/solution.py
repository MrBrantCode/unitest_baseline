"""
QUESTION:
Design a function named `find_longest_element` that takes a list of elements as input and returns the longest element, its index in the list, and the total number of occurrences of the longest element in the list. The list can contain elements of any type, including integers, floating-point numbers, and alphanumeric characters. The function should be able to handle a minimum of 100 elements and have a time complexity of O(n).
"""

def find_longest_element(lst):
    longest_element = ''
    longest_index = -1
    longest_count = 0
    
    for i, element in enumerate(lst):
        if len(str(element)) > len(longest_element):
            longest_element = str(element)
            longest_index = i
            longest_count = 1
        elif len(str(element)) == len(longest_element):
            longest_count += 1
    
    return longest_element, longest_index, longest_count