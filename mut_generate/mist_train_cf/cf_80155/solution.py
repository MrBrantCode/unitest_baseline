"""
QUESTION:
Implement a function named `binary_search` that performs a binary search on a sorted array `arr` to find the position of a given `target` number. The function should return a tuple containing the position of the target number and the number of iterations it took to find it. If the target number is not found, return 'Not Found'. The array `arr` is sorted in ascending order.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    count = 0

    while low <= high:
        count += 1
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            return mid, count
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return 'Not Found'