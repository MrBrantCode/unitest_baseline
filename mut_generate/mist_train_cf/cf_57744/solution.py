"""
QUESTION:
Write a function `remove_threes(arr)` that takes a multi-dimensional array `arr` as input and removes all occurrences of the number 3 at any level of the array. The function should handle nested lists and avoid out-of-bound errors or skipped elements.
"""

def remove_threes(arr):
    i = 0
    
    while i < len(arr):
        if isinstance(arr[i], list):  # If the current element is a list, recursively call the function
            remove_threes(arr[i])
            
            if not arr[i]:  # If empty list remains, remove it
                arr.pop(i)
                continue  # Skip to next iteration
        elif arr[i] == 3:  # If the current element is 3, remove it
            arr.pop(i)
            continue  # Skip to next iteration
        
        i += 1

    return arr