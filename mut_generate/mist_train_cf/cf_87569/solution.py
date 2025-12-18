"""
QUESTION:
Implement a function named `binary_search_rotated` that performs a binary search on a rotated sorted array to find the index of a given number. The function should take two parameters: `data` (the rotated sorted array) and `search_num` (the number to be searched). It should return the index of the `search_num` if found, otherwise return -1. The array is sorted in ascending order but rotated (i.e., shifted) an unknown number of times.
"""

def binary_search_rotated(data, search_num):
    low = 0
    high = len(data) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == search_num:
            return mid
        elif data[mid] >= data[low]:
            if search_num >= data[low] and search_num <= data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if search_num >= data[mid] and search_num <= data[high]:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1