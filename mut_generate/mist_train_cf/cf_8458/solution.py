"""
QUESTION:
Write a function called `binary_search` that performs binary search in a sorted array of integers and returns the indices of all occurrences of the target element. The array is sorted in ascending order and may contain duplicates. The function should have a time complexity of O(log n) and should not use any built-in functions or libraries for searching.
"""

def entance(arr, target):
    result = []
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result.append(mid)

            # Check if there are any occurrences of target to the left of the current index
            i = mid - 1
            while i >= left and arr[i] == target:
                result.append(i)
                i -= 1

            # Check if there are any occurrences of target to the right of the current index
            i = mid + 1
            while i <= right and arr[i] == target:
                result.append(i)
                i += 1

            return sorted(result)

        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result