"""
QUESTION:
Implement a function called `modified_binary_search` that takes a sorted array `arr` and a target element `target` as input and returns the number of occurrences of the target element in the array. The function should use a binary search approach to achieve this. The array can contain duplicate elements.
"""

def modified_binary_search(arr, target):
    def binary_search(arr, target, search_first):
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = (left + right) // 2

            if arr[mid] == target:
                result = mid
                if search_first:
                    right = mid - 1  # Search for the first occurrence
                else:
                    left = mid + 1   # Search for the last occurrence
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    first_occurrence = binary_search(arr, target, True)
    last_occurrence = binary_search(arr, target, False)

    if first_occurrence == -1:
        return 0
    else:
        return last_occurrence - first_occurrence + 1