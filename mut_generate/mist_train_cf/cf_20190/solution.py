"""
QUESTION:
Create a function `find_max_element` that takes a list of integers as input and returns the maximum element. The list will always contain at least two elements and the maximum element will always be unique. Do not use any built-in functions. The function should have a time complexity of O(n), where n is the length of the input list.
"""

def find_max_element(lst):
    max_element = lst[0]
    for element in lst:
        if element > max_element:
            max_element = element
    return max_element