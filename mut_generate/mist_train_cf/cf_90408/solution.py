"""
QUESTION:
Write a function called `binary_search` that performs binary search in a sorted array of integers. The function should take two parameters: a sorted array `arr` and a target integer `target`. It should return a list of indices of all occurrences of the target element in the array. If the target element is not found, the function should return an empty list. The time complexity of the function should be O(log n), where n is the size of the array.
"""

def binary_search(arr, target):
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