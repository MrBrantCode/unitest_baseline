"""
QUESTION:
Create a function `find_kth_smallest(arr, k)` that returns the kth smallest element in a sorted array of size n, where the function should have a time complexity of O(log n) and not use any additional space. The function should take two parameters: `arr` which is a sorted array of integers and `k` which is an integer representing the position of the element to be found.
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