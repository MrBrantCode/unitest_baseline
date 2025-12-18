"""
QUESTION:
Implement a function named `insertion_sort` that sorts an array of integers in ascending order. The array can contain up to 10^6 elements, including duplicates. The function should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        low, high = 0, i - 1
        
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] < key:
                low = mid + 1
            else:
                high = mid - 1

        for j in range(i, low, -1):
            arr[j] = arr[j - 1]

        arr[low] = key

    return arr