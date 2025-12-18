"""
QUESTION:
Implement a function `find_position` that takes a sorted numerical array and an integer value as arguments. The function should return the positional index of the integer within the numerical array using binary search. If the integer is not in the array, return the index position where the integer value would fit while maintaining the sort order of the array. The function should handle edge cases where the integer may not be in the array and may be larger than all numbers in the array.
"""

def find_position(sorted_arr, target):
    left, right = 0, len(sorted_arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_arr[mid] < target:
            left = mid + 1
        elif sorted_arr[mid] > target:
            right = mid - 1
        else:
            return mid
    return left