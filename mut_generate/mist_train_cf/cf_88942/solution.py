"""
QUESTION:
Write a function `remove_duplicates` that takes an array of up to 1000 elements (integers and strings) and returns a new array containing the unique elements from the original array, in the same order. The function should maintain the original order of elements and only keep the first occurrence of each element.
"""

def remove_duplicates(arr):
    unique_set = set()
    modified_arr = []

    for element in arr:
        if element not in unique_set:
            unique_set.add(element)
            modified_arr.append(element)

    return modified_arr