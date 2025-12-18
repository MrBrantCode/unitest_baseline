"""
QUESTION:
Write a function named `find_common_elements(arr1, arr2)` that takes two arrays of integers as input, and returns their common elements in ascending order without duplicates. The function should have a time complexity of less than O(n log n), where n is the length of the longer array.
"""

def find_common_elements(arr1, arr2):
    # Create a hash set to store unique elements from the first array
    unique_elements = set(arr1)

    # Initialize a list to store the common elements
    common_elements = []

    # Iterate through the second array
    for num in arr2:
        # Check if the element is present in the hash set
        if num in unique_elements:
            # Add the common element to the result list
            common_elements.append(num)

    # Sort the result list in ascending order and remove duplicates
    return sorted(list(set(common_elements)))