"""
QUESTION:
Implement a function binary_search that takes a sorted list of numbers, a target number, and a start and end index as input. It should recursively find the index of the first occurrence of the target number in the list using the binary search algorithm, with a time complexity of O(log n), where n is the size of the list. If the target number is not found, return -1.
"""

def entrance(data, target, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2
    if data[mid] == target:
        if mid > 0 and data[mid - 1] == target:
            return entrance(data, target, start, mid - 1)
        else:
            return mid
    elif data[mid] < target:
        return entrance(data, target, mid + 1, end)
    else:
        return entrance(data, target, start, mid - 1)