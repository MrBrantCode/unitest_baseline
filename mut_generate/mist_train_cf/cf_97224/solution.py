"""
QUESTION:
Write a function `find_common_elements(arr1, arr2)` that takes two arrays of integers `arr1` and `arr2` as input, and returns an array of common elements without duplicates in ascending order. The function should have a time complexity of less than O(n log n), where n is the length of the longer array.
"""

def find_common_elements(arr1, arr2):
    # Create a hash set to store unique elements from the first array
    unique_elements = set(arr1)

    # Initialize a list to store the common elements
    common_elements = []

    # Iterate through the second array
    for num in arr2:
        # Check if the element is present in the hash set
        if num in unique_elements and num not in common_elements:
            # Add the common element to the result list
            common_elements.append(num)

    # Sort the result list in ascending order
    common_elements.sort()

    return common_elements