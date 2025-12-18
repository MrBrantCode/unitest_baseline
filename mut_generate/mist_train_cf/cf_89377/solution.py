"""
QUESTION:
Write a recursive function named `find_duplicates` that takes an array of integers as input and returns a list of integers that appear more than once in the array. The function should return the elements in ascending order and should not contain any duplicate elements. The function should not use any built-in functions or libraries and should have a time complexity of less than O(n^2), where n is the length of the input array. The input array can have a maximum length of 10^5.
"""

def find_duplicates(arr):
    # Base case: if the array has less than 2 elements, return an empty list
    if len(arr) < 2:
        return []

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively find duplicates in the left and right halves
    left_duplicates = find_duplicates(left_half)
    right_duplicates = find_duplicates(right_half)

    # Merge and remove duplicate elements from the left and right duplicates
    merged_duplicates = merge_duplicates(left_duplicates, right_duplicates)

    # Count the occurrences of each element in the original array
    element_count = count_elements(arr)

    # Add the elements that appear more than once to the merged duplicates
    for element, count in element_count.items():
        if count > 1 and element not in merged_duplicates:
            merged_duplicates.append(element)

    # Sort and remove duplicate elements from the merged duplicates
    merged_duplicates.sort()

    return merged_duplicates


def merge_duplicates(duplicates1, duplicates2):
    # Merge two duplicate lists and remove duplicate elements
    merged_duplicates = duplicates1 + duplicates2
    merged_duplicates = remove_duplicates(merged_duplicates)

    return merged_duplicates


def count_elements(arr):
    # Count the occurrences of each element in the array
    element_count = {}
    for element in arr:
        element_count[element] = element_count.get(element, 0) + 1

    return element_count


def remove_duplicates(arr):
    # Remove duplicate elements from the array
    unique_elements = []
    for element in arr:
        if element not in unique_elements:
            unique_elements.append(element)

    return unique_elements