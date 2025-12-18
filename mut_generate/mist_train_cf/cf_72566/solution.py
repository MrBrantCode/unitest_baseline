"""
QUESTION:
Write a function `remove_duplicates` that takes an array of integers as input and returns the array with all duplicate elements removed. The function must maintain the original order of elements and not use additional data structures like sets or hash maps. The array length can be up to 10^5 and the elements are integers in the range [-10^3, 10^3].
"""

def remove_duplicates(arr):
    # Initialize an empty list to store unique elements
    unique_elements = []

    # Iterate over all elements in the input array
    for elem in arr:
        # If the current element is not already in unique_elements list, add it
        if elem not in unique_elements:
            unique_elements.append(elem)

    return unique_elements