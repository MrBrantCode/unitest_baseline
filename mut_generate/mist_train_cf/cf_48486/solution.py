"""
QUESTION:
Write a function named `binary_search` that takes a sorted array in ascending order and a target element as input, and returns the index of the target element in the array along with the number of iterations it took to find the element. If the target element is not found, the function should return -1 as the index and the total number of iterations.
"""

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0  

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid, count  

        count += 1   

    return -1, count  