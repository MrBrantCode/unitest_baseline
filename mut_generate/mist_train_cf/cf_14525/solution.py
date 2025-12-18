"""
QUESTION:
Write a function named `find_kth_smallest` that takes two parameters: a sorted array `arr` and an integer `k`, and returns the kth smallest element in the array. The function should have a time complexity of O(log n) and not use any additional space.
"""

def find_kth_smallest(arr, k):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
        count = 0

        for num in arr:
            if num <= arr[middle]:
                count += 1

        if count < k:
            low = middle + 1
        elif count >= k:
            high = middle - 1
        if count == k:
            return arr[middle]

    return -1