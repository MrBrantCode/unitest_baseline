"""
QUESTION:
Implement an iterative mergesort function, mergesort(arr), that takes an array of integers as input and returns the sorted array. The function should be able to handle large arrays of size up to 10^6 elements, including arrays with duplicate elements.
"""

def mergesort(arr):
    if len(arr) <= 1:
        return arr

    width = 1
    while width < len(arr):
        left = 0
        while left < len(arr):
            mid = left + width
            right = min(left + 2 * width, len(arr))

            # Merge subarrays arr[left:mid] and arr[mid:right]
            left_arr = arr[left:mid]
            right_arr = arr[mid:right]
            i = j = 0
            k = left

            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] <= right_arr[j]:
                    arr[k] = left_arr[i]
                    i += 1
                else:
                    arr[k] = right_arr[j]
                    j += 1
                k += 1

            while i < len(left_arr):
                arr[k] = left_arr[i]
                i += 1
                k += 1

            while j < len(right_arr):
                arr[k] = right_arr[j]
                j += 1
                k += 1

            left += 2 * width
        width *= 2

    return arr