"""
QUESTION:
Create a function named `circular_binary_search` that takes a circularly sorted list `data` and an integer `search_num` as inputs, and returns the index of `search_num` in the list if found, or -1 if not found. The function should use a binary search algorithm and handle the case where the pivot index of the circularly sorted list is unknown. The function should assume that the list does not contain any duplicate values.
"""

def circular_binary_search(data, search_num):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == search_num:
            return mid
        
        # if the first half is sorted
        if data[low] <= data[mid]:
            # and target is in the first half
            if data[low] <= search_num < data[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            # else the second half is sorted
            # and target is in the second half
            if data[mid] < search_num <= data[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1