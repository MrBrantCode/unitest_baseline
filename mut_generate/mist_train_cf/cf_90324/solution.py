"""
QUESTION:
Perform binary search on a given sorted list of numbers to find the index of the first occurrence of a target number and the total number of occurrences of the target number. If the target number is not present, return -1 as the first occurrence and 0 as the total occurrences.

Function: `binary_search(arr, target)`

Restrictions: The input list `arr` must be sorted in ascending order.
"""

def entance(arr, target):
    left = 0
    right = len(arr) - 1
    first_occurrence = -1
    total_occurrences = 0

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            first_occurrence = mid
            total_occurrences += 1

            # Check if there are more occurrences to the left
            i = mid - 1
            while i >= 0 and arr[i] == target:
                total_occurrences += 1
                i -= 1

            # Check if there are more occurrences to the right
            i = mid + 1
            while i < len(arr) and arr[i] == target:
                total_occurrences += 1
                i += 1

            break
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if first_occurrence != -1:
        return first_occurrence, total_occurrences
    else:
        return -1, 0