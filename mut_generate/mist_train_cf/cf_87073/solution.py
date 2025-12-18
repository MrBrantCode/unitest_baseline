"""
QUESTION:
Write a Python function `find_max_elements` that takes a 2-dimensional array as input, finds the maximum element in each row that is divisible by 3, and returns a list of these maximum elements. If no such element exists in a row, include the smallest possible integer value in the output list for that row.
"""

def find_max_elements(array):
    max_elements = []
    for row in array:
        max_element = float('-inf')
        for element in row:
            if element % 3 == 0 and element > max_element:
                max_element = element
        max_elements.append(max_element)
    return max_elements