"""
QUESTION:
Create a function `remove_duplicates(arr)` that removes duplicate elements from the given array while maintaining their original order. The function should not use any additional data structures and have a time complexity of O(n^2). The input array can contain any type of elements and may be empty. The function should return the array with unique elements.
"""

def remove_duplicates(arr):
    # Traverse the array
    for i in range(len(arr)):
        j = i + 1
        # Compare each element with all the elements after it
        while j < len(arr):
            # If a duplicate element is found, remove it
            if arr[i] == arr[j]:
                arr.pop(j)
            else:
                j += 1
    return arr