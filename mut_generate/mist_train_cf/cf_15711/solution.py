"""
QUESTION:
Write a function `remove_duplicates(arr)` that removes duplicate elements from a given array `arr`. The function should not use any built-in functions or libraries for removing duplicates or any additional data structures. The time complexity should be O(n^2) or less.
"""

def remove_duplicates(arr):
    # Check each element in the array
    for i in range(len(arr)):
        # Check if the current element is already seen
        is_duplicate = False
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                is_duplicate = True
                break

        # If duplicate is found, remove it from the array
        if is_duplicate:
            arr = arr[:j] + arr[j+1:]
    
    return arr