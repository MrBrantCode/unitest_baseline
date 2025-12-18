"""
QUESTION:
Implement a function `binary_search_rotated` that performs a binary search on a rotated sorted array. The function should take two parameters: a list of integers `data` and an integer `search_num`. It should return the index of `search_num` in `data` if found, otherwise -1. The array `data` is sorted in ascending order but rotated at some pivot point.
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