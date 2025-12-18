"""
QUESTION:
Write a recursive function called `find_duplicates` that takes a list of integers as input, and returns a list of integers that appear more than once in the input list. The returned list should be in ascending order and should not contain any duplicate elements. The function should not use any built-in functions or libraries and should have a time complexity less than O(n^2), where n is the length of the input list. The input list will have a maximum length of 10^5.
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

    # Sort and return the merged duplicates
    merged_duplicates.sort()
    return merged_duplicates


def merge_duplicates(duplicates1, duplicates2):
    # Merge two duplicate lists and remove duplicate elements
    merged_duplicates = list(set(duplicates1 + duplicates2))
    return merged_duplicates


def count_elements(arr):
    # Count the occurrences of each element in the array
    element_count = {}
    for element in arr:
        element_count[element] = element_count.get(element, 0) + 1

    return element_count