"""
QUESTION:
Implement a function named `linearSearch` that performs a case-sensitive linear search on a sorted array of unique elements. The input array must be in ascending order and cannot exceed a length of 1000. The function should return the index of the search element if found, and -1 otherwise.
"""

def linearSearch(search_element, input_array):
    for i in range(len(input_array)):
        if input_array[i] == search_element:
            return i
    return -1