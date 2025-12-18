"""
QUESTION:
Write a function named `binary_search` that takes a sorted list of integers and a target number as input. The function should return the index of the first occurrence of the target number if it exists in the list, and -1 otherwise. The function should have a time complexity of O(log n), where n is the length of the list.
"""

def binary_search(sorted_list, target_number):
    start = 0
    end = len(sorted_list) - 1

    while start <= end:
        mid = (start + end) // 2
        if sorted_list[mid] == target_number:
            if mid == 0 or sorted_list[mid-1] < target_number:
                return mid
            else:
                end = mid - 1
        elif sorted_list[mid] < target_number:
            start = mid + 1
        else:
            end = mid - 1

    return -1