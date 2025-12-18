"""
QUESTION:
Implement the function `find_largest_elements(arr)` that finds all elements in the given array which are larger than both their immediate neighbours and all their non-immediate neighbours. The function should use a divide and conquer approach with a time complexity of O(log n).
"""

def find_largest_elements(arr):
    result = []

    def binary_search(arr, low, high):
        if low > high:
            return

        mid = low + (high - low) // 2

        if mid > 0 and mid < len(arr) - 1 and arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:

            if (mid - 2 < 0 or arr[mid] > arr[mid-2]) and (mid + 2 >= len(arr) or arr[mid] > arr[mid+2]):
                result.append(arr[mid])

        binary_search(arr, low, mid-1)

        binary_search(arr, mid+1, high)

    binary_search(arr, 0, len(arr)-1)

    return result