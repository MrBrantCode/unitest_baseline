"""
QUESTION:
Write a function `common_elements` that takes two lists `arr1` and `arr2` as input and returns a list of elements that are common to both lists, in the order they appear in `arr1`. The function should work with lists containing any hashable data types, such as integers, strings, and tuples.
"""

def common_elements(arr1, arr2):
    return [element for element in arr1 if element in arr2]