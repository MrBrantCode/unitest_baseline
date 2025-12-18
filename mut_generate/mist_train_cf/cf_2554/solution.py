"""
QUESTION:
Create a function `find_common_elements(arr1, arr2)` that compares two given arrays and finds the common elements present in both while maintaining their relative order. The function should handle duplicate elements by removing them from the final result. The time complexity of the solution should be O(n), where n is the length of the longer array. The space complexity should be O(m), where m is the number of unique common elements between the two arrays. The function should be case-sensitive when comparing elements, and the output array should be sorted in descending order. It should also handle negative numbers, non-integer elements, and arrays with duplicate elements efficiently.
"""

def find_common_elements(arr1, arr2):
    # Create a set to store unique elements in arr2
    unique_elements = set(arr2)

    # Create a list to store common elements in descending order
    common_elements = []

    # Iterate over arr1 and check if each element is in the unique_elements set
    for num in arr1:
        if num in unique_elements:
            # Add the common element to the common_elements list
            common_elements.append(num)

            # Remove the element from the set to handle duplicates
            unique_elements.remove(num)

    # Sort the common_elements list in descending order
    common_elements.sort(reverse=True)

    return common_elements