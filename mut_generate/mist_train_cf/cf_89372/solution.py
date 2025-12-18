"""
QUESTION:
Create a function named `binary_search` that takes in a sorted list `arr`, a goal value `goal`, and a comparison function `compare_fn` as parameters. The `compare_fn` function compares two elements and returns a negative number if the first element is less than the second, 0 if they are equal, and a positive number if the first element is greater than the second. The function should return the index of `goal` if it is present in the list, or -1 if it is not found. If the goal value appears multiple times in the list, the function can return the index of any occurrence.
"""

def binary_search(arr, goal, compare_fn):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        compare_result = compare_fn(arr[mid], goal)
        
        if compare_result == 0:
            return mid
        elif compare_result < 0:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1