"""
QUESTION:
Write a function `insert_into_array(arr, target)` that inserts a `target` integer into an array of integers `arr` in ascending order. If there are duplicate `target` integers in the array, insert the `target` integer immediately after the last occurrence of the `target` integer. The function should return the modified array. The time complexity of the solution should be optimized for the given task.
"""

def insert_into_array(arr, target):
    index = len(arr)
    
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            index = i + 1
            break
        elif arr[i] < target:
            index = i + 1
            break
    
    arr.insert(index, target)
    return arr