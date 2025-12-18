"""
QUESTION:
Implement a function `binary_search` that performs a binary search on a sorted list to find the index of a target number. The function should take a sorted list of unique integers and a target number as input and return the index of the target number if found, or None otherwise.
"""

def binary_search(sorted_list, target):
    start = 0
    end = len(sorted_list) - 1

    while start <= end:
        middle = (start + end) // 2

        # If the middle element is the target, return its index
        if sorted_list[middle] == target:
            return middle

        # If the target is smaller than the middle element, ignore the right half
        elif sorted_list[middle] > target:
            end = middle - 1

        # If the target is greater than the middle element, ignore the left half
        else:
            start = middle + 1
    # If the number doesn't exist, return None
    return None