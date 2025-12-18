"""
QUESTION:
Write a recursive function called BinarySearch that implements the binary search algorithm. The function should take four parameters: a sorted array, a target value to search for, and two indices representing the start and end of the part of the array to be searched. If the target value is found, return its index; otherwise, return "Not Found". Ensure the function works correctly and efficiently, with a time complexity of O(log N).
"""

def BinarySearch(array, target, start, end):
    if end < start:
        return "Not Found"
    
    mid = (start + end) // 2
    
    if array[mid] > target:
        return BinarySearch(array, target, start, mid - 1)
    elif array[mid] < target:
        return BinarySearch(array, target, mid + 1, end)
    else:
        return mid