"""
QUESTION:
Write a function `insert_in_sorted` that inserts a new element into a sorted array in ascending order, considering duplicate elements, while optimizing for time complexity. The input array and the target element are given, and the function should return the updated array. The array can contain duplicate elements and should maintain its sorted order after insertion.
"""

def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (right + left) // 2
        if array[mid] == target:
            return mid  
        elif array[mid] < target:
            left = mid + 1  
        else:
            right = mid - 1  
    return left  

def insert_in_sorted(array, target):
    pos = binary_search(array, target)
    array.insert(pos, target)
    return array