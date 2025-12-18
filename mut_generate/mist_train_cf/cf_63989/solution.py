"""
QUESTION:
Write a function called `find_common_elements` that takes two lists of elements as input and returns a list of elements that appear in both input lists, with each element appearing the exact number of times it appears in both lists.
"""

def find_common_elements(arr1, arr2):
    common_elements = []
    for element in arr1:
        if element in arr2:
            common_elements.append(element)
            arr2.remove(element)
    return common_elements