"""
QUESTION:
Implement a function named `insertion_sort` that sorts an array of integers in ascending order using the insertion sort algorithm with a binary search to optimize performance. The input array can contain up to 10^6 integers and may have duplicate values. The implementation should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        low, high = 0, i - 1
        
        # Use binary search to find the correct position for the key
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1

        # Shift the elements to the right to make space for the key
        for j in range(i, low, -1):
            arr[j] = arr[j - 1]

        # Insert the key into its correct position
        arr[low] = key

    return arr