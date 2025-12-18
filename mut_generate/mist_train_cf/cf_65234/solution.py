"""
QUESTION:
Implement a function named `solve(arr, target)` that takes an array of integers `arr` and a target integer `target` as input. The function should eliminate duplicate elements from `arr`, sort the resulting array in non-descending order, and then use a binary search algorithm to find the lowest index of the first occurrence of `target` in the sorted array. If `target` is not found, the function should return -1.
"""

def solve(arr, target):
    # Eliminating redundancy by using Set data structure in Python
    unique_arr = list(set(arr))
    
    # Sorting the array in non-descending order
    unique_arr.sort()
    
    # Implementing Binary Search
    left, right = 0, len(unique_arr)-1
    while left <= right:
        mid = (left + right) // 2
        if unique_arr[mid] == target:
            return mid  # Return the index of the target
        elif unique_arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    # If the element is not found
    return -1