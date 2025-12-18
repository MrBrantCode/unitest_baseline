"""
QUESTION:
Create a function `compress_and_sort(arr1, arr2)` that combines two input arrays `arr1` and `arr2`, returns a new array with only unique elements sorted in ascending order, and also returns the total count of unique elements in both input arrays. If there are ties, the smallest number should come first.
"""

def compress_and_sort(arr1, arr2):
    combined = arr1 + arr2   # combine the two lists
    unique_elements = list(set(combined))  # create a list of unique elements
    unique_elements.sort()  # sort the unique elements
    count = len(unique_elements)   # count the unique elements
    return unique_elements, count