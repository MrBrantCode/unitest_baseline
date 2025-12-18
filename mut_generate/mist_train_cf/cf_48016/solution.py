"""
QUESTION:
Write a function named `binary_search` that performs a binary search on an array of integers. The array is not initially sorted and may contain duplicate values. The function should return the index of the first occurrence of the target value in the array if found, or -1 if not found.
"""

def binary_search(arr, x):
    arr.sort()
    low = 0
    high = len(arr) - 1
    first_occurrence = -1

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller or equal, ignore right half
        else:
            if arr[mid] == x: 
                first_occurrence = mid 
            high = mid - 1

    # Return first occurrence of x
    return first_occurrence