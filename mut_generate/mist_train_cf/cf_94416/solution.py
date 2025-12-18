"""
QUESTION:
Implement the function `search_indices(arr, target)` that searches for a particular element (`target`) in a sorted array (`arr`) and returns a list of indices of all occurrences of the element. If the element is not found, return an empty list. The function should have a time complexity of O(log n) in the worst case scenario. The input array can contain duplicate elements and its size can be up to 10^6.
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