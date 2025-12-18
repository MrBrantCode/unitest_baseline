"""
QUESTION:
Create a function called `find_common_elements` that takes two sorted arrays of integers as input and returns a new array containing their common elements with no duplicates. The function should have a time complexity of O(log n), where n is the length of the longer array.
"""

def find_common_elements(arr1, arr2):
    """
    Returns a new array containing the common elements of two sorted arrays.

    Args:
        arr1 (list): The first sorted array of integers.
        arr2 (list): The second sorted array of integers.

    Returns:
        list: A new array containing the common elements with no duplicates.
    """
    common_elements = []
    start = 0
    end = len(arr2) - 1

    for element in arr1:
        # Perform binary search on arr2
        while start <= end:
            mid = (start + end) // 2

            if arr2[mid] == element:
                if element not in common_elements:
                    common_elements.append(element)
                break
            elif arr2[mid] < element:
                start = mid + 1
            else:
                end = mid - 1
        start = 0
        end = len(arr2) - 1

    return common_elements