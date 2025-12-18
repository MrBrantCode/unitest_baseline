"""
QUESTION:
Implement a function `merge_sort(arr)` that sorts an array of integers using a modified merge sort algorithm. The algorithm should recursively divide the input array into smaller subarrays until each subarray has a length of 1 or less, and then merge these sorted subarrays while using binary search to find the correct position for each element from the right subarray in the left subarray. The input array can contain duplicate elements. The function should return the sorted array.

Restrictions: 
- The input array only contains integers.
- The function should use a recursive approach to divide the array into smaller subarrays.
- The function should use binary search to find the correct position for each element from the right subarray in the left subarray during the merge process.
"""

def merge_sort(arr):
    def binary_search(left, target, start):
        low = start
        high = len(left) - 1

        while low <= high:
            mid = (low + high) // 2

            if left[mid] == target:
                return mid
            elif left[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low

    def merge(left, right):
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                pos = binary_search(left, right[j], i)
                result.extend(left[i:pos])
                result.append(right[j])
                i = pos
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)