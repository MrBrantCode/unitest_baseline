"""
QUESTION:
Create a function called `find_unique_elements` that takes an array as input and returns a list of elements that appear only once in the array. The function should return all unique elements, regardless of their position or order in the input array.
"""

def find_unique_elements(arr):
    unique_elements = []
    for elem in arr:
        if arr.count(elem) == 1:
            unique_elements.append(elem)
    return unique_elements