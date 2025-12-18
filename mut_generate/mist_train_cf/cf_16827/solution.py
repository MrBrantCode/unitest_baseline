"""
QUESTION:
Create a function named `search_indices` that takes a sorted array and a target element as input, and returns a list of indices where the target element is found in the array. The function should achieve this in a time complexity of O(log n) in the worst-case scenario. If the element is not found, return an empty list.
"""

def search_indices(arr, target):
    indices = []
    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            indices.append(mid)
            left, right = mid - 1, mid + 1

            while left >= start and arr[left] == target:
                indices.append(left)
                left -= 1

            while right <= end and arr[right] == target:
                indices.append(right)
                right += 1

            return sorted(indices)

        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return indices